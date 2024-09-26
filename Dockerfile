FROM python:3.11.1-slim-buster

ENV HOME=/root

RUN apt-get update && apt-get install -y libssl-dev libcurl4-openssl-dev python3-dev gcc curl
RUN curl -sSL https://install.python-poetry.org | python - --version 1.3.1
WORKDIR /app
COPY ./pyproject.toml /app
COPY ./poetry.lock /app
ENV PATH="${HOME}/.local/bin:$PATH"
RUN ${HOME}/.local/bin/poetry --version
RUN ${HOME}/.local/bin/poetry config virtualenvs.create false
RUN ${HOME}/.local/bin/poetry install
COPY ./app /app
ENTRYPOINT ["/root/.local/bin/poetry", "run", "python", "-m", "app.app"]
