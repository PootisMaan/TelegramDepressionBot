from peewee import SqliteDatabase, Model, TextField, PrimaryKeyField, DateField, IntegerField
from datetime import datetime

db = SqliteDatabase('Depression_test_bot.db')


class Test(Model):
    id = PrimaryKeyField(unique=True)
    user_id = IntegerField()
    result = TextField()
    date = DateField(default=datetime.utcnow())

    class Meta:
        database = db
        order_by = 'date'
        db_table = 'tests'
