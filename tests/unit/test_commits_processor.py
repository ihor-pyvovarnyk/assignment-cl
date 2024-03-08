from unittest.mock import Mock

import pytest
from git import GitCommandError

from assignment_cl.commits_processor import CommitsProcessor
from assignment_cl.input_extractor import BaseInputExtractor
from assignment_cl.patch_loader import BasePatchLoader


def test_commits_processor():
    input_extractor = Mock(
        spec=BaseInputExtractor,
        __iter__=lambda self: iter(
            [
                "https://github.com/ihor-pyvovarnyk/distributed-web-scraper-server/commit/fbaee753365a163566dc1ef5df06dbc1a896f00c",  # noqa
                "https://github.com/ihor-pyvovarnyk/distributed-web-scraper-server/commit/ca820708c47384e7cd1886988d037f1b2d2ac4d9",  # noqa
            ]
        ),
    )
    patch_loader = Mock(spec=BasePatchLoader)

    CommitsProcessor(input_extractor, patch_loader).run()

    assert patch_loader.save.call_count == 2


def test_commits_processor_unprocessable_commit_url():
    input_extractor = Mock(
        spec=BaseInputExtractor,
        __iter__=lambda self: iter(
            ["https://example.com/account/project/commit/fbaee753365a163566dc1ef5df06dbc1a896f00c"]
        ),
    )
    patch_loader = Mock(spec=BasePatchLoader)

    with pytest.raises(ValueError):
        CommitsProcessor(input_extractor, patch_loader).run()


def test_commits_processor_unable_to_create_patch(mocker):
    input_extractor = Mock(
        spec=BaseInputExtractor,
        __iter__=lambda self: iter(
            [
                "https://github.com/ihor-pyvovarnyk/distributed-web-scraper-server/commit/fbaee753365a163566dc1ef5df06dbc1a896f00c",  # noqa
                "https://github.com/ihor-pyvovarnyk/distributed-web-scraper-server/commit/ca820708c47384e7cd1886988d037f1b2d2ac4d9",  # noqa
            ]
        ),
    )
    patch_loader = Mock(spec=BasePatchLoader)
    commits_processor = CommitsProcessor(input_extractor, patch_loader)
    mocker.patch.object(commits_processor, "_get_patch_content_for_commit", side_effect=GitCommandError([""]))

    commits_processor.run()

    assert patch_loader.save.call_count == 0
