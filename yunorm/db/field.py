# coding=utf-8
import datetime


class Prikey(object):
    pass


class Field(object):

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)


class CharField(Field):

    def __init__(self, default=None, null=False):
        Field.__init__(self, null=null, default=default)


class DecimalField(Field):

    def __init__(self, default=None, null=False):
        Field.__init__(self, default=default, null=null)


class IntegerField(Field):

    def __init__(self, default=None, null=False):
        # msyql既然支持int转换,就用一下吧
        default = str(default)
        Field.__init__(self, default=default, null=null)


class DateTimeField(Field):

    def __init__(self, default=None, auto_now_add=False, null=False):
        if auto_now_add:
            default = str(datetime.datetime.now())
        Field.__init__(self, default=default, null=null)
