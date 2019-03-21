import time
import datetime
import traceback
from yunorm.db import models
from yunorm.db import field

CE_DB = {
    'host': '10.10.10.10',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'database': 'ce',
    'charset': 'utf8mb4'
}

GOLD_DB = {
    'host': '127.0.0.1',
    'port': 32768,
    'user': 'root',
    'password': 'root',
    'database': 'gold_price',
    'charset': 'utf8mb4'
}


class Feed(models.Model):
    # 你可能有多个字段，但是你不用全都定义在这，在这定义的字段都是你要展示的字段
    # 不在这定义字段并不影响下边的筛选，当然你只能筛选数据表中存在的字段
    url = field.CharField()
    name = field.CharField()
    descp = field.CharField()
    zan_num = field.IntegerField()
    like_num = field.IntegerField()
    create_time = field.DateTimeField()

    class meta:
        db_config = CE_DB
        db_table = 'feed'


class GoldPrice(models.Model):
    gold = field.DecimalField()
    create_time = field.DateTimeField()

    class meta:
        db_config = GOLD_DB
        db_table = 'price'


def get_feed_by_id():
    feed = Feed.objects.filter(id=3700000).first().data()
    print("Feed:", feed.name)


def get_feed_by_dict():
    filter_dict = {
        "zan_num__gt": 0,
        "id__gt": 3700000
    }
    feeds = Feed.objects.filter(**filter_dict).limit(1, 2).data()
    for feed in feeds:
        print(feed.name)


def create_gold_price():
    create_data = {
        'gold': 1.10,
        'create_time': str(datetime.datetime.now())
    }
    GoldPrice.create(**create_data)


def update_gold_price():
    update_data = {
        'gold': 1.10,
        'create_time': str(datetime.datetime.now())
    }
    res = GoldPrice.objects.filter(id__in=[1, 2]).data()
    for r in res:
        r.update(**update_data)
    res = GoldPrice.objects.filter(id=3).first().data()
    if res:
        res.update(**update_data)


def delete_gold_price():
    res = GoldPrice.objects.filter(id__in=[7, 8]).data()
    for r in res:
        result = r.delete()
        print(result)


def get_gold_price():
    price = GoldPrice.objects.filter(id=1).first().data()
    print("GoldPrice:", price.create_time)


if __name__ == "__main__":
    print("--------feed------")
    get_feed_by_id()
    get_feed_by_dict()
    print("-------gold------")
    create_gold_price()
    update_gold_price()
    get_gold_price()
    delete_gold_price()
    print(traceback.format_exc())
