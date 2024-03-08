import os.path
from abc import ABC, abstractmethod

from assignment_cl.commit_url_wrappers.base import BaseCommitUrl


class BasePatchLoader(ABC):
    @abstractmethod
    def save(self, commit: BaseCommitUrl, patch_content: str) -> None: ...


class LocalPatchLoader(BasePatchLoader):
    def __init__(self, output_dir: str):
        self.output_dir = output_dir

    def save(self, commit: BaseCommitUrl, patch_content: str) -> None:
        patch_file_name = self._get_output_file_name_for_commit(commit)
        with open(patch_file_name, "w") as f:
            f.write(patch_content)

    def _get_output_file_name_for_commit(self, commit: BaseCommitUrl) -> str:
        if commit.account:
            file_name = f"{commit.account}_{commit.project_name}_{commit.commit_hash}.patch"
        else:
            file_name = f"{commit.project_name}_{commit.commit_hash}.patch"
        return os.path.join(self.output_dir, file_name)
