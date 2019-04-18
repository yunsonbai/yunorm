from yunorm.db import models
from yunorm.db import field

CE_DB = {
    'host': '10.x.x.x',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'database': 'ce',
    'charset': 'utf8mb4',
    'pool_size': 10,
}


class Feed(models.Model):
    url = field.CharField()
    name = field.CharField()
    descp = field.CharField()
    zan_num = field.IntegerField()
    like_num = field.IntegerField()
    create_time = field.DateTimeField()

    class meta:
        db_config = CE_DB
        db_table = 'feed'
