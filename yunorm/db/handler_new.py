# coding=utf-8
import mysql.connector.pooling
import random


class DbHandler(object):

    def __init__(self, **db_config):
        self.db_config = db_config
        self.pool_size = self.db_config.get('pool_size', 1)
        self.mysql_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name=self.db_config.get('database', 'test'),
            **self.db_config)

    def get_conn(self):
        return

    def execute(self, *args, fetchall=True):
        conn = self.mysql_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(*args)
        if fetchall:
            data = cursor.fetchall()
        else:
            data = cursor.fetchone()
        cursor.close()
        conn.close()
        return data


class _DbHandlers(object):

    def __init__(self):
        self.dbhanders = {}

    def set_dbhandler(self, key, config):
        self.dbhanders[key] = DbHandler(**config)

    def get_dbhandler(self, key):
        return self.dbhanders[key]

    @staticmethod
    def instance():
        if not hasattr(_DbHandlers, '_instance'):
            _DbHandlers._instance = _DbHandlers()
        return _DbHandlers._instance


DbHandlers = _DbHandlers.instance()
