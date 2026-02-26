# Stage 1: Build
FROM python:3.11-slim AS builder

WORKDIR /app
COPY pyproject.toml README.md LICENSE ./
COPY src/ src/

RUN pip install --no-cache-dir build && \
    python -m build --wheel

# Stage 2: Runtime
FROM python:3.11-slim

RUN useradd -m rekon
WORKDIR /workspace

COPY --from=builder /app/dist/*.whl /tmp/
RUN pip install --no-cache-dir /tmp/*.whl && \
    rm /tmp/*.whl

USER rekon

ENTRYPOINT ["rekon"]
CMD ["chat"]
