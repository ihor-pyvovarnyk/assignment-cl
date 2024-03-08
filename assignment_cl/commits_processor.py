from itertools import groupby
from tempfile import TemporaryDirectory
from typing import Iterator

import click
from git import GitCommandError, Repo

from assignment_cl.commit_url_wrappers import ALL_COMMIT_URL_WRAPPERS
from assignment_cl.commit_url_wrappers.base import BaseCommitUrl
from assignment_cl.input_extractor import BaseInputExtractor, TxtInputExtractor
from assignment_cl.patch_loader import BasePatchLoader, LocalPatchLoader


class CommitsProcessor:
    @classmethod
    def create(cls, input_file: str, output_dir: str) -> "CommitsProcessor":
        # NOTE: This is a bit of an overengineering in this case, but here you go,
        #       inverted dependencies and a shortcut factory method
        return cls(TxtInputExtractor(input_file), LocalPatchLoader(output_dir))

    def __init__(self, input_extractor: BaseInputExtractor, patch_loader: BasePatchLoader):
        self.input_extractor = input_extractor
        self.patch_loader = patch_loader

    def run(self) -> None:
        commits = self._get_commits()
        for repo_url, grouped_commits in groupby(commits, lambda c: c.repo_url):
            click.echo(f"Cloning {repo_url}...")
            with TemporaryDirectory() as repo_dir:
                repo = Repo.clone_from(repo_url, repo_dir)
                for commit in grouped_commits:
                    click.echo(f"\tCreating patch for commit {commit.commit_hash}")
                    try:
                        patch_content = self._get_patch_content_for_commit(repo, commit)
                    except GitCommandError:
                        click.echo(f"Unable to identify commit {commit.commit_hash} in the repository")
                        continue
                    self.patch_loader.save(commit, patch_content)

    def _get_commits(self) -> Iterator[BaseCommitUrl]:
        for commit_url in self.input_extractor:
            try:
                yield next(
                    instance
                    for commit_url_wrapper in ALL_COMMIT_URL_WRAPPERS
                    if (instance := commit_url_wrapper.create_if_commit_url_acceptable(commit_url))
                )
            except StopIteration:
                raise ValueError(f"Don't have commit URL wrapper for {commit_url}")

    @staticmethod
    def _get_patch_content_for_commit(repo: Repo, commit: BaseCommitUrl) -> str:
        return repo.git.format_patch("-1", "--stdout", commit.commit_hash)
