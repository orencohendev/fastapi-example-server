

start:
	@poetry run python -m app.app

test:
	@poetry run pytest

lint:
	@poetry run black app

type:
	@poetry run mypy app