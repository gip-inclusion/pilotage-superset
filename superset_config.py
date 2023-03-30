import os

_conn_str = (
    os.getenv("SQLALCHEMY_DATABASE_URI") or os.getenv("POSTGRESQL_ADDON_URI") or ""
)
SQLALCHEMY_DATABASE_URI = _conn_str.replace('"', "").replace("'", "")

ENABLE_PROXY_FIX = True
PROXY_FIX_CONFIG = {
    "x_for": 1,
    "x_proto": 0,
    "x_host": 1,
    "x_port": 0,
    "x_prefix": 0,
}

FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True,
    "EMBEDDABLE_CHARTS": True,
    "DASHBOARD_RBAC": True,
}

# Almost like Gamma, but we removed
#     "Can share Dahsboard"
#     "Can share chart"
#     "Can explore json on superset"
#     "Can explore on superset"
#     "Can save on superset"
#     "Can copy on superset"
# TODO(vperron): Create the "embed" role at startup ?
# It seems that `superset fab` can import role files.
# We can also just acknowledge that this is a production setting ?
GUEST_ROLE_NAME = "Embed"
GUEST_TOKEN_JWT_SECRET = os.getenv("GUEST_TOKEN_JWT_SECRET")

TALISMAN_ENABLED = True
TALISMAN_CONFIG = {
    "content_security_policy": {
        "default-src": ["'self'", "'unsafe-inline'", "'unsafe-eval'"],
        "img-src": ["'self'", "'unsafe-inline'", "data:"],
        "worker-src": ["'self'", "blob:"],
        "connect-src": [
            "'self'",
            "https://api.mapbox.com",
            "https://events.mapbox.com",
        ],
        "object-src": "'none'",
        "frame-src": ["'self'", "http://127.0.0.1:8000"],
        "frame-ancestors": ["'self'", "http://127.0.0.1:8000"],
    }
}


REDIS_URL = os.getenv("REDIS_URL")
if REDIS_URL:
    from datetime import timedelta

    CACHE_CONFIG = {
        "CACHE_TYPE": "RedisCache",
        "CACHE_DEFAULT_TIMEOUT": int(timedelta(days=1).total_seconds()),
        "CACHE_KEY_PREFIX": "superset_cache_",
        "CACHE_REDIS_URL": f"{REDIS_URL}/0",
    }

    # Cache for datasource metadata and query results
    DATA_CACHE_CONFIG = {
        "CACHE_TYPE": "RedisCache",
        "CACHE_DEFAULT_TIMEOUT": int(timedelta(days=1).total_seconds()),
        "CACHE_KEY_PREFIX": "superset_data_",
        "CACHE_REDIS_URL": f"{REDIS_URL}/0",
    }

    FILTER_STATE_CACHE_CONFIG = {
        "CACHE_TYPE": "RedisCache",
        "CACHE_DEFAULT_TIMEOUT": int(timedelta(days=1).total_seconds()),
        "CACHE_KEY_PREFIX": "superset_filter_",
        "CACHE_REDIS_URL": f"{REDIS_URL}/0",
    }

    EXPLORE_FORM_DATA_CACHE_CONFIG = {
        "CACHE_TYPE": "RedisCache",
        "CACHE_DEFAULT_TIMEOUT": int(timedelta(days=1).total_seconds()),
        "CACHE_KEY_PREFIX": "superset_explore_",
        "CACHE_REDIS_URL": f"{REDIS_URL}/0",
    }
