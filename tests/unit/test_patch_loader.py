import os.path
from tempfile import TemporaryDirectory
from unittest.mock import Mock

import pytest

from assignment_cl.patch_loader import LocalPatchLoader


@pytest.mark.parametrize(
    "commit_mock,target_file_name",
    [
        (
            Mock(
                account="account",
                project_name="project",
                commit_hash="fbaee753365a163566dc1ef5df06dbc1a896f00c",
            ),
            "account_project_fbaee753365a163566dc1ef5df06dbc1a896f00c.patch",
        ),
        (
            Mock(
                account=None,
                project_name="project",
                commit_hash="fbaee753365a163566dc1ef5df06dbc1a896f00c",
            ),
            "project_fbaee753365a163566dc1ef5df06dbc1a896f00c.patch",
        ),
    ],
)
def test_local_patch_loader(commit_mock, target_file_name):
    patch_content = "fakefakefake"

    with TemporaryDirectory() as temp_dir:
        loader = LocalPatchLoader(temp_dir)
        loader.save(commit_mock, patch_content)

        with open(os.path.join(temp_dir, target_file_name)) as f:
            assert f.read() == patch_content
