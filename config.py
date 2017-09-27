import os
import peewee_async


BASE_DIR = os.getcwd()

# peewee_async 连接池对象
# peewee_async 连接池
database = peewee_async.PooledMySQLDatabase('aiohttp_data', **{
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'port': 3306,
})
objects = peewee_async.Manager(database)
# objects.database.allow_sync = False
