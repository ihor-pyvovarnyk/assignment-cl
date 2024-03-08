import re
from functools import cached_property

from assignment_cl.commit_url_wrappers.base import BaseRegExParsedCommitUrl


class FfmpegCommitUrl(BaseRegExParsedCommitUrl):
    ALLOWED_URL_PATTERN = re.compile(
        r"(?P<base_url>https?://git\.ffmpeg\.org)/gitweb/(?P<project>[^/]+).git/commit/(?P<commit_hash>[0-9a-f]{40})",
        re.IGNORECASE,
    )

    @cached_property
    def repo_url(self) -> str:
        return f"{self.base_url}/{self.project_name}.git"


class FreedesktopCommitUrl(BaseRegExParsedCommitUrl):
    ALLOWED_URL_PATTERN = re.compile(
        r"(?P<base_url>https?://cgit\.freedesktop\.org)/"
        r"((?P<account>[^/]+)/)?(?P<project>[^/]+)/commit/?\?[^\?]*id=(?P<commit_hash>[0-9a-f]{40})",
        re.IGNORECASE,
    )

    @cached_property
    def repo_url(self) -> str:
        new_base_url = self.base_url.replace("://cgit", "://anongit")
        if self.account:
            return f"{new_base_url}/git/{self.account}/{self.project_name}.git"
        else:
            return f"{new_base_url}/git/{self.project_name}.git"


class GitHubCommitUrl(BaseRegExParsedCommitUrl):
    ALLOWED_URL_PATTERN = re.compile(
        r"(?P<base_url>https?://github\.com)/"
        r"(?P<account>[^/]+)/(?P<project>[^/]+)/commit/(?P<commit_hash>[0-9a-f]{40})",
        re.IGNORECASE,
    )

    @cached_property
    def repo_url(self) -> str:
        return f"{self.base_url}/{self.account}/{self.project_name}.git"


class GitLabCommitUrl(BaseRegExParsedCommitUrl):
    ALLOWED_URL_PATTERN = re.compile(
        r"(?P<base_url>https?://gitlab[^/]+)/"
        r"(?P<account>[^/]+)/(?P<project>[^/]+)/-/commit/(?P<commit_hash>[0-9a-f]{40})",
        re.IGNORECASE,
    )

    @cached_property
    def repo_url(self) -> str:
        return f"{self.base_url}/{self.account}/{self.project_name}.git"


class GlusterCommitUrl(BaseRegExParsedCommitUrl):
    ALLOWED_URL_PATTERN = re.compile(
        r"(?P<base_url>https?://git\.gluster\.org)/cgit/(?P<project>[^/]+/?[^/]+).git/"
        r"commit/?\?[^\?]*id=(?P<commit_hash>[0-9a-f]{40})",
        re.IGNORECASE,
    )

    @cached_property
    def repo_url(self) -> str:
        # NOTE: Couldn't find any link to the repo on that website, so had to improvise
        return f"https://github.com/gluster/{self.project_name}.git"


class GnuSavannahCommitUrl(BaseRegExParsedCommitUrl):
    ALLOWED_URL_PATTERN = re.compile(
        r"(?P<base_url>https?://git\.savannah\.gnu\.org)/cgit/"
        r"((?P<account>[^/]+)/)?(?P<project>[^/]+).git/commit/?\?[^\?]*id=(?P<commit_hash>[0-9a-f]{40})",
        re.IGNORECASE,
    )

    @cached_property
    def repo_url(self) -> str:
        if self.account:
            return f"{self.base_url}/git/{self.account}/{self.project_name}.git"
        else:
            return f"{self.base_url}/git/{self.project_name}.git"


class OpensslCommitUrl(BaseRegExParsedCommitUrl):
    ALLOWED_URL_PATTERN = re.compile(
        r"(?P<base_url>https?://git\.openssl\.org)/gitweb/?"
        r"\?[^\?]*p=(?P<project>[^;]+).git[^\?]*h=(?P<commit_hash>[0-9a-f]{40})",
        re.IGNORECASE,
    )

    @cached_property
    def repo_url(self) -> str:
        # NOTE: Couldn't find any link to the repo on that website, so had to improvise
        return f"https://github.com/openssl/{self.project_name}.git"


class PostgresqlCommitUrl(BaseRegExParsedCommitUrl):
    ALLOWED_URL_PATTERN = re.compile(
        r"(?P<base_url>https?://git\.postgresql\.org)/gitweb/?"
        r"\?[^\?]*p=(?P<project>[^;]+).git[^\?]*h=(?P<commit_hash>[0-9a-f]{40})",
        re.IGNORECASE,
    )

    @cached_property
    def repo_url(self) -> str:
        return f"{self.base_url}/git/{self.project_name}.git"


class QtCommitUrl(BaseRegExParsedCommitUrl):
    ALLOWED_URL_PATTERN = re.compile(
        r"(?P<base_url>https?://code\.qt\.io)/cgit/"
        r"(?P<account>[^/]+)/(?P<project>[^/]+/?[^/]+).git/commit/?\?[^\?]*id=(?P<commit_hash>[0-9a-f]{40})",
        re.IGNORECASE,
    )

    @cached_property
    def repo_url(self) -> str:
        return f"{self.base_url}/{self.account}/{self.project_name}.git"


class SourcewareCommitUrl(BaseRegExParsedCommitUrl):
    ALLOWED_URL_PATTERN = re.compile(
        r"(?P<base_url>https?://sourceware\.org)/git/gitweb\.cgi/?"
        r"\?[^\?]*p=(?P<project>[^;]+).git[^\?]*h=(?P<commit_hash>[0-9a-f]{40})",
        re.IGNORECASE,
    )

    @cached_property
    def repo_url(self) -> str:
        return f"{self.base_url}/git/{self.project_name}.git"
