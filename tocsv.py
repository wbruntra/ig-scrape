import csv
import json
import datetime

username = 'cristiano'

with open(username + '/' + username + '.json') as f:
    posts = json.loads(f.read())

post = posts[0]

fields = ['edge_media_preview_like', 'edge_media_to_comment', 'text','time']


def getData(post):
    result = [
        post["edge_media_preview_like"]["count"],
        post["edge_media_to_comment"]["count"],
        post["edge_media_to_caption"]["edges"][0]["node"]["text"],
        datetime.datetime.fromtimestamp(
        int(post["taken_at_timestamp"])
        ).strftime('%Y-%m-%d %H:%M:%S')
    ]
    return result

with open(username + '-posts.csv', 'w') as csvfile:
    fields = ['likes', 'comments', 'caption','time']
    writer = csv.writer(csvfile)
    writer.writerow(fields)
    for post in posts:
        writer.writerow(getData(post))
