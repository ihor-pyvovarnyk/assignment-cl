from unittest.mock import Mock

import pytest

from assignment_cl.utils import timeit


def test_timeit_success(mocker):
    click = mocker.patch("assignment_cl.utils.click")
    func = Mock()

    decorated_func = timeit(func)
    assert decorated_func() == func.return_value

    click.echo.assert_called()


def test_timeit_failure(mocker):
    click = mocker.patch("assignment_cl.utils.click")
    func = Mock(side_effect=ValueError())

    decorated_func = timeit(func)
    with pytest.raises(ValueError):
        decorated_func()

    click.echo.assert_called()
