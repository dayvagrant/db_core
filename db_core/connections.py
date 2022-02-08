import boto3
from infi.clickhouse_orm.database import Database
from pymongo import MongoClient
from sqlalchemy import create_engine

from db_core.utils import CONFIG


def get_sqlalchemy_engine(driver, user, pwd, host, port, database):
    """Generate engine using sqlalchemy."""
    conn_string = "{driver}://{user}:{pwd}@{host}:{port}/{database}".format(
        driver=driver,
        user=user,
        pwd=pwd,
        host=host,
        port=port,
        database=database,
    )
    engine = create_engine(conn_string)
    return engine


def get_mongo_client():
    """Make connection to Mongo database."""
    mongo_config = "mongodb"
    client = MongoClient(
        "{driver}://{user}:{pwd}@{host}:{port}/{auth}".format(
            driver="mongodb",
            user=CONFIG.get(mongo_config, "user"),
            pwd=CONFIG.get(mongo_config, "pwd"),
            host=CONFIG.get(mongo_config, "host"),
            port=CONFIG.get(mongo_config, "port"),
            auth="?authSource=admin",
        )
    )
    return client


def get_clickhouse_client(database):
    """Make connection to Mongo database."""
    click_config = "clickhouse"
    database = Database(
        database,
        db_url="http://{host}:{port}".format(
            host=CONFIG.get(click_config, "host"),
            port=CONFIG.get(click_config, "port"),
        ),
        username=CONFIG.get(click_config, "user"),
        password=CONFIG.get(click_config, "pwd"),
    )
    return database


def get_aws_s3_client():
    """Make connection to AWS S3"""
    s3_config = "aws-s3"
    client = boto3.client(
        "s3",
        endpoint_url=CONFIG.get(s3_config, "url"),
        region_name="ru-1a",
        aws_access_key_id=CONFIG.get(s3_config, "login"),
        aws_secret_access_key=CONFIG.get(s3_config, "password"),
    )
    return client


def get_postgres_engine():
    """Make connection to database."""
    postgres_config = "postgres"
    engine = get_sqlalchemy_engine(
        driver="postgresql+psycopg2",
        user=CONFIG.get(postgres_config, "user"),
        pwd=CONFIG.get(postgres_config, "pwd"),
        host=CONFIG.get(postgres_config, "host"),
        port=CONFIG.get(postgres_config, "port"),
        database=CONFIG.get(postgres_config, "db"),
    )
    return engine
