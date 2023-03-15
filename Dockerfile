FROM apache/superset:24c472a4a3bbbc83f49942c5e77ad466519df74c

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    git \
    && apt-get autoremove -yqq --purge \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

USER superset

RUN pip install --no-cache-dir psycopg2-binary

COPY superset_config.py .
COPY entrypoint.sh .

CMD ["bash", "-c", "./entrypoint.sh"]

