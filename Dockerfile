FROM python:3.12-alpine
LABEL maintainer="Vaddi"
# label app maintainer's name
ENV PYTHONBUFFERED 1
#output directly without delay 

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false 
RUN apk add --update --no-cache python3-dev libffi-dev bash postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \    
    /venv/bin/pip install -r /tmp/requirements.txt && \
    if [ "$DEV" = "true" ]; then \ 
        /venv/bin/pip install -r /tmp/requirements.dev.txt; \
    fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        vaddi

ENV PATH="/venv/bin:$PATH"
USER vaddi



