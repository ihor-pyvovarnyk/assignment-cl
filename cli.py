import click

from assignment_cl.commits_processor import CommitsProcessor
from assignment_cl.utils import timeit


@click.command(
    help="Clone repositories for provided commit urls and create patch files of the commits in the output directory"
)
@click.option(
    "-i",
    "--input-file",
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
    help="Input file with commit URLs",
)
@click.option(
    "-o",
    "--output-dir",
    type=click.Path(exists=True, file_okay=False, dir_okay=True),
    help="Output directory to load patch files to",
)
@timeit
def save_patches_cmd(input_file: str, output_dir: str) -> None:
    CommitsProcessor.create(input_file, output_dir).run()


if __name__ == "__main__":
    save_patches_cmd()
