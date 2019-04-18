# coding=utf-8
import MySQLdb
import random


class DbHandler(object):

    def __init__(self, **db_config):
        self.db_config = db_config
        self.conns = []
        self.pool_size = self.db_config.get('pool_size', 1)
        for i in range(self.pool_size):
            self.conns.append(self._get_conn())

    def _get_conn(self):
        autocommit = self.db_config.get("autocommit", True)
        database = self.db_config.get('database', 'test')
        conn = MySQLdb.connect(
            host=self.db_config.get('host', 'localhost'),
            port=self.db_config.get('port', 3306),
            user=self.db_config.get('user', 'root'),
            passwd=self.db_config.get('password', ''),
            db=database,
            charset=self.db_config.get('charset', 'utf8'),
            autocommit=autocommit
        )
        conn.select_db(database)
        return conn

    def get_conn(self):
        try:
            conn = self.conns.pop()
            conn.ping()
        except Exception as e:
            conn = self._get_conn()
        self.conns.append(conn)
        return conn

    def execute(self, *args, fetchall=True):
        cursor = self.get_conn().cursor()
        cursor.execute(*args)
        if fetchall:
            data = cursor.fetchall()
        else:
            data = cursor.fetchone()
        cursor.close()
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
