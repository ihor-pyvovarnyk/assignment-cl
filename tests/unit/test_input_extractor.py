from tempfile import NamedTemporaryFile

from assignment_cl.input_extractor import TxtInputExtractor


def test_txt_input_extractor():
    with NamedTemporaryFile(mode="w") as fake_txt_file:
        fake_txt_file.write(
            "https://github.com/ihor-pyvovarnyk/distributed-web-scraper-server/commit/fbaee753365a163566dc1ef5df06dbc1a896f00c"  # noqa
        )
        fake_txt_file.write("\n# https://example.com")
        fake_txt_file.write("\n")
        fake_txt_file.flush()

        extractor = TxtInputExtractor(fake_txt_file.name)
        assert list(extractor) == [
            "https://github.com/ihor-pyvovarnyk/distributed-web-scraper-server/commit/fbaee753365a163566dc1ef5df06dbc1a896f00c"  # noqa
        ]
