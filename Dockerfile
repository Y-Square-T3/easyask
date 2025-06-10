FROM python:3.12-bookworm

WORKDIR /app

COPY . .

RUN uv lock && uv sync

EXPOSE 8080

CMD ["uv", "run", "server.py"]
