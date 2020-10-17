## Para lista de tweets

`15 13 * * * nohup python3 science-pulse-tweets/pulse_tweets.py pt morning > sci_out_pt_morn.log 2> sci_err_pt_morn.log &`

`0 14 * * * nohup python3 science-pulse-tweets/pulse_tweets.py en morning > sci_out_en_morn.log 2> sci_err_en_morn.log &`

`15 23 * * * nohup python3 science-pulse-tweets/pulse_tweets.py pt night > sci_out_pt_night.log 2> sci_err_pt_night.log &`

`0 0 * * * nohup python3 science-pulse-tweets/pulse_tweets.py en night > sci_out_en_night.log 2> sci_err_pt_night.log &`

## Para lista de hashtags

`0 18 * * * nohup python3 science-pulse-tweets/pulse_hashtags.py pt day > sci_hash_pt.log 2> sci_hash_err_pt.log &`

`0 19 * * * nohup python3 science-pulse-tweets/pulse_hashtags.py en day > sci_hash_en.log 2> sci_hash_err_en.log &`
