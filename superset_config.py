import os

_conn_str = os.getenv("SQLALCHEMY_DATABASE_URI") or os.getenv("POSTGRESQL_ADDON_URI") or ""
SQLALCHEMY_DATABASE_URI = _conn_str.replace('"', '').replace("'", '')

ENABLE_PROXY_FIX = True
PROXY_FIX_CONFIG = {
    "x_for": 1,
    "x_proto": 0,
    "x_host": 1,
    "x_port": 0,
    "x_prefix": 0,
}
