from peewee import *
import json

with open("config.json") as jsonfile:
    # `json.loads` parses a string in json format
    db_config = json.load(jsonfile)['database']

database = PostgresqlDatabase(
    db_config['dbname'], **{'host': db_config['host'], 'port': db_config['port'], 'user': db_config['user'], 'password': db_config['password']})


class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Base(BaseModel):

    class Meta:
        table_name = 'base'
        schema = 'public'
        primary_key = False

class BaseBackup(BaseModel):

    class Meta:
        table_name = 'base_backup'
        schema = 'public'
        primary_key = False

class Experts(BaseModel):
    account_created_at = DateTimeField(null=True)
    account_lang = BooleanField(null=True)
    description = TextField(null=True)
    favourites_count = IntegerField(null=True)
    followers_count = IntegerField(null=True)
    friends_count = IntegerField(null=True)
    listed_count = IntegerField(null=True)
    location = TextField(null=True)
    name = TextField(null=True)
    profile_background_url = TextField(null=True)
    profile_banner_url = TextField(null=True)
    profile_expanded_url = TextField(null=True)
    profile_image_url = TextField(null=True)
    profile_url = TextField(null=True)
    protected = BooleanField(null=True)
    screen_name = TextField(null=True)
    sqn_n = IntegerField(null=True)
    statuses_count = IntegerField(null=True)
    url = TextField(null=True)
    user_id = TextField(null=True)
    verified = BooleanField(null=True)

    class Meta:
        table_name = 'experts'
        schema = 'public'
        primary_key = False

class Retweets(BaseModel):

    class Meta:
        table_name = 'retweets'
        schema = 'public'
        primary_key = False

class TweetBotParams(BaseModel):
    body_text = CharField()
    description = CharField()
    lang = CharField()
    param_id = AutoField()
    period_day = CharField()
    slug = CharField()

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

class TweetProperties(BaseModel):

    class Meta:
        table_name = 'tweet_properties'
        schema = 'public'
        primary_key = False

class Tweets(BaseModel):

    class Meta:
        table_name = 'tweets'
        schema = 'public'
        primary_key = False

class TwitterLangs(BaseModel):

    class Meta:
        table_name = 'twitter_langs'
        schema = 'public'
        primary_key = False

class TwitterSources(BaseModel):

    class Meta:
        table_name = 'twitter_sources'
        schema = 'public'
        primary_key = False

class TwitterUsers(BaseModel):

    class Meta:
        table_name = 'twitter_users'
        schema = 'public'
        primary_key = False