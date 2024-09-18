FROM python:3.12-alpine
LABEL maintainer = "Vaddi"
# label app maintainer's name
ENV PYTHONBUFFERED 1
#output directly without delay 

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
        --disable-password \
        --no-create-home \
        vaddi

ENV PATH="/venv/bin:$PATH"
USER vaddi



