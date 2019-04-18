from db import models


def get_feed(feed_id):
    feed = models.Feed.objects.filter(id=feed_id).first().data()
    return feed.name
