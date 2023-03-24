FROM apache/superset:24c472a4a3bbbc83f49942c5e77ad466519df74c

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    git \
    vim \
    && apt-get autoremove -yqq --purge \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

USER superset

RUN pip install --no-cache-dir psycopg2-binary

COPY --chown=superset:root superset_config.py .
COPY --chown=superset:root entrypoint.sh .

CMD ["bash", "-c", "./entrypoint.sh"]

