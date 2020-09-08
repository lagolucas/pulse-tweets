from peewee import *
import json

with open("config.json") as jsonfile:
    # `json.loads` parses a string in json format
    db_config = json.load(jsonfile)['database']

database = PostgresqlDatabase(
    'postgres', **{'host': db_config['host'], 'port': db_config['port'], 'user': db_config['user'], 'password': db_config['password']})


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class TweetBotParams(BaseModel):
    body_text = CharField()
    description = CharField()
    lang = CharField()
    param_id = AutoField()
    slug = CharField()
    thread_begin = CharField()
    thread_end = CharField()

    class Meta:
        table_name = 'tweet_bot_params'
        schema = 'public'


class TweetBotQueue(BaseModel):
    bot_flag = BooleanField(null=True)
    created_at = DateTimeField()
    handle = CharField(null=True)
    param = ForeignKeyField(column_name='param_id', field='param_id', model=TweetBotParams)
    queue_id = BigAutoField()
    status_id = BigIntegerField()
    trend_type = IntegerField()

    class Meta:
        table_name = 'tweet_bot_queue'
        schema = 'public'