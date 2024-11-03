FROM python:3.11

RUN mkdir -p /favoritefilms

WORKDIR /favoritefilms

COPY . .

RUN pip install poetry
RUN poetry install

CMD bash -c "poetry run alembic upgrade head && poetry run python -m main"
