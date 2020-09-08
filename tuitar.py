if __name__ == '__main__':
    from database import TweetBotParams
    from database import TweetBotQueue
    import twitter

    params = TweetBotParams.select().where(TweetBotParams.slug == 'start')   
    for param in params:
    # Para cada parâmetro de "start" do science pulse

        # Iniciar o fio naquela lingua
        # twitter.start_thread(param)
        
        # Coletar todos os tweets para lista naquela lingua
        tweets = TweetBotQueue.select(TweetBotQueue, TweetBotParams).join(TweetBotParams).where(TweetBotQueue.param.lang == param.lang)

        for tweet in tweets:
            print(tweet.status_id)

        # Para cada tweet

            # Coletar os parâmetros necessários para fazer o QuoteTweet

            # Postar o Quote Tweet

        # Encerrar a lista naquela lingua


    # print("iniciando a coleta de arrobas para tuitar")
    # arrobas = database.get_handles_to_tweet()

    # print("Coletados " + str(len(arrobas)) + " arrobas para tuitar...")

    # print("iniciando processo de tuites... ")
    # twitter.tweet_start()

    # qtde_tweets = 0
    # for arroba in arrobas:
    #     tweet_ids = database.get_tweets_ids(arroba)
    #     last_tweet = twitter.tweet_start_arroba(arroba, len(tweet_ids))
    #     for tweet_id in tweet_ids:
    #         qtde_tweets += 1
    #         id, tweet, handle, archive_url, creation_date = database.retrieve_tweet(tweet_id)
    #         last_tweet = twitter.tweet(handle, tweet, archive_url, creation_date, id, last_tweet)
    #         if not qtde_tweets%20:
    #             time.sleep(3600)
        
    #     database.update_tweeted(tweet_ids)
    #     twitter.tweet_end_arroba(arroba, last_tweet)

    # twitter.tweet_end(qtde_tweets)
