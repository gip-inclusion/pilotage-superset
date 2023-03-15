#!/bin/bash

set -e
set -x

BASE_DIR=$(pwd)

superset fab create-admin \
              --username admin \
              --firstname Superset \
              --lastname Admin \
              --email admin@superset.com \
              --password "${SUPERSET_ADMIN_PASSWORD}"

superset db upgrade

if [[ "$SUPERSET_LOAD_EXAMPLES" == "1" ]]; then
	superset load_examples
fi

superset init

superset run -h 0.0.0.0 -p 8080 --with-threads
