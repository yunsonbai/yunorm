# coding=utf-8
import six
from yunorm.db.error import *
from yunorm.db.field import (Prikey, Field)
from yunorm.db.handler import DbHandlers
from yunorm.db.sql import QuerySet
from yunorm.utils import tools


class MetaModel(type):
    db_key = None
    db_table = None
    fields = {}
    db_config = {}

    def __init__(cls, name, bases, attrs):
        super(MetaModel, cls).__init__(name, bases, attrs)
        fields = {}
        pri_field = 'id'
        fields['id'] = Prikey()
        for key, val in cls.__dict__.items():
            if isinstance(val, Prikey):
                fields.pop(pri_field)
                fields[key] = val
                pri_field = key

            elif isinstance(val, Field):
                fields[key] = val
            else:
                pass
        cls.fields = fields
        cls.pri_field = pri_field
        cls.attrs = attrs
        cls.objects = cls()
        if 'meta' in dir(cls):
            cls.db_table = cls.meta.db_table
            cls.db_config = cls.meta.db_config
            cls.db_key = tools.get_md5(
                '{}{}{}'.format(
                    cls.db_config['host'], cls.db_config['port'],
                    cls.db_config['database']))
            DbHandlers.set_dbhandler(cls.db_key, cls.db_config)


@six.add_metaclass(MetaModel)
class Model(object):

    @classmethod
    def create(self, **kwargs):
        '''
        function:
            create one or more data
        params:
            dict
        '''
        for key, val in kwargs.items():
            if val is None or key not in self.fields:
                raise Exception(NORIGHTERROR.format(key))
        for key, val in self.fields.items():
            if isinstance(val, Field):
                if key not in kwargs:
                    if val.default:
                        kwargs[key] = val.default
                    elif val.null:
                        kwargs[key] = None
                    else:
                        raise Exception(FEILDNULLRROR.format(key))
        _keys = []
        _values = []
        for key, value in kwargs.items():
            _keys.append(key)
            _values.append(value)
        sql = 'insert into {0}({1}) values ({2});'.format(
            self.db_table, ','.join(_keys), ','.join(['%s']*len(_keys)))
        result = DbHandlers.get_dbhandler(self.db_key).execute(sql, _values)
        return result

    def _update_delete_where(self, values, **kwargs):
        for key, val in kwargs.items():
            if val is None or key not in self.fields:
                raise Exception(NORIGHTERROR.format(key))
        where = 'where {0} = %s'.format(self.pri_field)
        values.append(self.__dict__[self.pri_field])
        return where, values

    def update(self, **kwargs):
        '''
        function:
            update data
        params:
            dict
        '''
        _values = []
        _keys = []
        for key, value in kwargs.items():
            _keys.append('{0} = %s'.format(key))
            _values.append(value)
        where, _values = self._update_delete_where(_values, **kwargs)

        sql = 'update {0} set {1} {2};'.format(
            self.db_table, ','.join(_keys), where)
        return DbHandlers.get_dbhandler(self.db_key).execute(sql, _values)

    def delete(self, **kwargs):
        _values = []
        where, _values = self._update_delete_where(_values, **kwargs)
        sql = 'delete from {0} {1};'.format(self.db_table, where)
        try:
            result = DbHandlers.get_dbhandler(
                self.db_key).execute(sql, _values)
            if not result._info:
                setattr(result, 'success', True)
        except:
            result = object()
            setattr(result, 'success', True)
        return result

    def filter(self, **kwargs):
        '''
        function:
            add filter conditions
        '''
        return QuerySet(self, kwargs)
