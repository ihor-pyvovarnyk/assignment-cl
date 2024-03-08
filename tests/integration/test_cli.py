import os
from tempfile import NamedTemporaryFile, TemporaryDirectory

import pytest
from click.testing import CliRunner

from cli import save_patches_cmd


@pytest.fixture
def commit_urls():
    return [
        "https://github.com/ihor-pyvovarnyk/distributed-web-scraper-server/commit/fbaee753365a163566dc1ef5df06dbc1a896f00c",  # noqa
        "https://github.com/ihor-pyvovarnyk/distributed-web-scraper-server/commit/ca820708c47384e7cd1886988d037f1b2d2ac4d9",  # noqa
    ]


@pytest.fixture
def input_file(commit_urls):
    with NamedTemporaryFile("w") as f:
        f.write("\n".join(commit_urls))
        f.flush()
        yield f


@pytest.fixture
def output_dir():
    with TemporaryDirectory() as temp_output_dir:
        yield temp_output_dir


def test_save_patches_cmd(input_file, output_dir):
    runner = CliRunner()
    result = runner.invoke(save_patches_cmd, ["-i", input_file.name, "-o", output_dir])
    assert result.exit_code == 0
    assert os.listdir(output_dir) == [
        "ihor-pyvovarnyk_distributed-web-scraper-server_fbaee753365a163566dc1ef5df06dbc1a896f00c.patch",
        "ihor-pyvovarnyk_distributed-web-scraper-server_ca820708c47384e7cd1886988d037f1b2d2ac4d9.patch",
    ]
