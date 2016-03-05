import json
from twitter import *

def Connect_Twitter(key_file):
    with open(key_file) as f:
        secretjson = json.load(f)

    t = Twitter(auth = OAuth(secretjson["access_token"], secretjson["access_token_secret"], secretjson["consumer_key"], secretjson["consumer_key_secret"]))

    return t
