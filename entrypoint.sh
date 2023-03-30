#!/bin/bash

set -e
set -x

BASE_DIR=$(pwd)

if [[ "$SUPERSET_INIT" == "1" ]]; then
	superset fab create-admin \
				--username admin \
				--firstname Superset \
				--lastname Admin \
				--email admin@superset.com \
				--password "${SUPERSET_ADMIN_PASSWORD}"

	superset fab import-roles --path embed-role.json
	superset db upgrade
	superset init
fi

if [[ "$SUPERSET_LOAD_EXAMPLES" == "1" ]]; then
	superset load_examples
fi

gunicorn \
	--bind "0.0.0.0:8080" \
	--limit-request-field_size 0 \
	--limit-request-line 0 \
	--statsd-host "localhost:8125" \
	--timeout 120 \
	--worker-connections 1000 \
	--workers 4 \
	--worker-class gevent \
	"superset.app:create_app()"
