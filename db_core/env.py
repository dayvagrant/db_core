"""Set of configrations."""

_CONFIGS = {
    "postgres": {
        "host": "0.0.0.0",
        "port": "5432",
        "user": <USER>,
        "pwd": <USER>,
        "db": "postgres",
    },
    "mongodb": {
        "host": "0.0.0.0",
        "port": "27017",
        "user": <USER>,
        "pwd": <PASS>,
    },
    "clickhouse": {
        "host": "0.0.0.0",
        "port": "8123",
        "user": <USER>,
        "pwd": <PASS>,
        "db": "db_live",
    },
     "aws-s3": {
        "url": <URL>,
        "login": <USER>,
        "password": <PASS>,
    },

}
