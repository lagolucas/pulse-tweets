if __name__ == '__main__':
    from database import TweetBotParams
    from database import TweetBotQueue
    import twitter
    import sys

    languages = ['pt', 'en']

    for language in languages:
        first = True
        previous_status = None

        # first_tweet = TweetBotParams.select().where((TweetBotParams.slug == 'start') 
        #     & (TweetBotParams.lang == language) 
        #     & (TweetBotParams.period_day == sys.argv[1])).get()
        # previous_status = twitter.start_thread(first_tweet)

        status_list = TweetBotQueue.select(TweetBotQueue, TweetBotParams).join(TweetBotParams).where(
            (TweetBotQueue.param.lang == language) 
            & (TweetBotParams.period_day == sys.argv[1]) 
            & (TweetBotQueue.bot_flag == False)).order_by(TweetBotQueue.trend_type.asc())

        for status in status_list:
            previous_status = twitter.tweet(status, previous_status, first)
            # print(status.param.body_text)
            # print(status.handle)
            first = False
            status.bot_flag = True
            status.save()

        last_tweet = TweetBotParams.select().where((TweetBotParams.slug == 'end') &
                                                   (TweetBotParams.lang == language)).get()
        twitter.end_thread(last_tweet, previous_status)
        print(last_tweet.body_text)
