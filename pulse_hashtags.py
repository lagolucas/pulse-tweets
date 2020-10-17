if __name__ == '__main__':
    from database import TweetBotParams
    from database import HashtagBotQueue
    import twitter
    import sys

    languages = [sys.argv[1]]

    for language in languages:

        hashtags = HashtagBotQueue.select(HashtagBotQueue, TweetBotParams).join(TweetBotParams).where(
            (HashtagBotQueue.param.lang == language)
            & (HashtagBotQueue.param.period_day == sys.argv[2])
            & (HashtagBotQueue.bot_flag == False)).order_by(HashtagBotQueue.ranking.asc())

        param = TweetBotParams.get(
            (TweetBotParams.period_day == sys.argv[2]) 
            & (TweetBotParams.lang == language) 
            & (TweetBotParams.slug == 'hashtag'))

        twitter.tweet_hashtags(param, hashtags)

        for hashtag in hashtags:
            hashtag.bot_flag = True
            hashtag.save()
