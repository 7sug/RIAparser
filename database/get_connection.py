import psycopg2 as psycopg2
import json


def connection(database, user, password, host, port):
    con = psycopg2.connect(
        database=database,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print("connected!")
    return con


def config_reader(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = json.load(f)
    con = connection(text["database"], text["user"], text["password"], text["host"], text["port"])
    return con
