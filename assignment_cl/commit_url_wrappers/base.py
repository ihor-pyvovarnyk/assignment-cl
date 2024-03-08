import re
import urllib.parse
from abc import ABC, abstractmethod
from functools import cached_property
from typing import Optional


class BaseCommitUrl(ABC):

    @classmethod
    @abstractmethod
    def create_if_commit_url_acceptable(cls, commit_url: str) -> Optional["BaseCommitUrl"]: ...

    def __init__(self, commit_url: str) -> None:
        self.commit_url = commit_url

    def __str__(self) -> str:
        return f"<{self.__class__.__name__} {self.commit_hash}>"

    def __repr__(self) -> str:
        return str(self)

    @cached_property
    def url_parts(self) -> urllib.parse.ParseResult:
        return urllib.parse.urlparse(self.commit_url)

    @cached_property
    def base_url(self) -> str:
        return urllib.parse.urlunparse(self.url_parts._replace(path="", params="", query="", fragment=""))

    @cached_property
    def account(self) -> str | None:
        return None

    @cached_property
    @abstractmethod
    def project_name(self) -> str: ...

    @cached_property
    def commit_hash(self) -> str:
        return re.search(r"[0-9a-f]{7,40}", self.commit_url, re.IGNORECASE)[0]

    @cached_property
    @abstractmethod
    def repo_url(self) -> str: ...


class BaseRegExParsedCommitUrl(BaseCommitUrl):
    ALLOWED_URL_PATTERN = re.compile(
        r"(?P<base_url>https?://example.com)/((?P<account>[^/]+)/)?(?P<project>[^/]+)/(?P<commit_hash>[0-9a-f]{40})",
        re.IGNORECASE,
    )

    @classmethod
    def create_if_commit_url_acceptable(cls, commit_url: str):
        if match := cls._regex_match(commit_url):
            return cls(commit_url, match)

    def __init__(self, commit_url: str, regex_match: re.Match | None = None) -> None:
        super().__init__(commit_url)
        self.regex_match = regex_match or self._regex_match(commit_url)

    @classmethod
    def _regex_match(cls, commit_url: str) -> re.Match | None:
        return re.search(cls.ALLOWED_URL_PATTERN, commit_url)

    @cached_property
    def base_url(self) -> str:
        return self.regex_match.group("base_url")

    @cached_property
    def account(self) -> str | None:
        try:
            return self.regex_match.group("account")
        except IndexError:
            return None

    @cached_property
    def project_name(self) -> str:
        return self.regex_match.group("project")

    @cached_property
    def commit_hash(self) -> str:
        return self.regex_match.group("commit_hash")
