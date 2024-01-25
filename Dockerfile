FROM  python:3.12.1-slim-bookworm AS build
RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes python3-venv gcc libpython3-dev && \
    python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip setuptools wheel

FROM build as build-venv
COPY requirements.txt /requirements.txt
RUN /venv/bin/pip install --disable-pip-version-check -r /requirements.txt

# Copy the virtualenv into a distroless image
FROM python:3.12.1-alpine3.19
COPY --from=build-venv /venv /venv
COPY src/ /app
WORKDIR /app
ENTRYPOINT ["/venv/bin/python3", "main.py"]
