from datetime import datetime
from typing import Any, Callable

import click


def timeit(func: Callable) -> Callable:
    def inner(*args: Any, **kwargs: Any) -> Any:
        start_time = datetime.now()
        try:
            return func(*args, **kwargs)
        finally:
            click.echo(f"Execution time: {datetime.now() - start_time}")

    return inner
