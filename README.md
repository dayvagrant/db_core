# db_core

## Table of Contents

- [About](#about)
- [Usage](#usage)

## About <a name = "about"></a>

Database connectors for some types.

## Added connections and engines:
- sqlalchemy engine
- postgres
- mongoClient
- clickhouse
- aws-s3


### Dependencies

What things you need to install the software and how to install them.

```
pip install poetry
```

### Installing

1. clone repo from github

```
git clone https://github.com/dayvagrant/db_core.git
```

2. change you db config in db_core.env.py

3. usage with poetry

```
poetry install
```

## Usage <a name = "usage"></a>



```
from db_core.connections import get_postgres_engine

client = get_postgres_engine(
    database_name='test_db'
    )
with client.connect() as conn:
    ...
```
