FROM python:3.12-bookworm

WORKDIR /app

COPY . .

RUN uv lock && uv sync

CMD ["uv", "run", "main.py"]
