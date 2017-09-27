from peewee import *
from config import database


class User(Model):
    username = CharField(max_length=50, unique=True)
    password = CharField(max_length=50)

    class Meta:
        database = database

if __name__ == '__main__':
    User.create_table(True)
