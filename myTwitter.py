import json
from twitter import *
import csv


"""
key_file requires Twitter 4 tokens
(access_token, access_token_secret, consumer_key, consumer_key_secret)
"""
def connect_twitter(key_file):
    with open(key_file) as f:
        secretjson = json.load(f)

    t = Twitter(auth = OAuth(secretjson["access_token"], 
                             secretjson["access_token_secret"], 
                             secretjson["consumer_key"], 
                             secretjson["consumer_key_secret"]))

    return t


"""
token:Twitter OAuthed object
temp_since_id:search tweet from temp_since_id
"""
def search_recent_tweet(token, query, temp_since_id):
    apiresults = token.search.tweets(q=query, 
                                     lang="ja", 
                                     since_id = temp_since_id, 
                                     result_type="recent", 
                                     count=100)

    return apiresults


"""
filename:save filename
apiresults:tweet search data
csv outputs timestamp, twitter id, tweet text.
"""
def write_csv(filename, apiresults):
    f_csv = open("./{}.csv".format(filename), 'a')
    f_json = open("./{}.json".format(filename), 'a')
    f_log = open("./{}_log".format(filename),'a')

    if len(apiresults["statuses"]) != 0:
        for i in range(len(apiresults["statuses"])):
            date = apiresults["statuses"][i]["created_at"]
            name = apiresults["statuses"][i]["user"]["screen_name"]
            text = apiresults["statuses"][i]["text"]
            row = (date, name, text)
            csv.writer(f_csv).writerow(row)

    json.dump(apiresults, f_json, indent = 4)
    f_log.write(str(len(apiresults["statuses"]))+'\n')
    f_log.write(str(apiresults["search_metadata"]["since_id"])+'\n')
    f_log.write(str(apiresults["search_metadata"]["max_id"])+'\n')
  
    f_csv.close()
    f_json.close()
    f_log.close()
