activate_venv:
	poetry shell

install:
	poetry install

lint:
	flake8 assignment_cl/ tests/ cli.py
	isort --check-only --diff --stdout .
	black --diff .

format:
	isort .
	black .

test:
	pytest tests --cov=assignment_cl

unit_test:
	pytest tests/unit --cov=assignment_cl

integration_test:
	pytest tests/integration --cov=assignment_cl
