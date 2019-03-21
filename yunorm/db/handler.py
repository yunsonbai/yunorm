# coding=utf-8
import MySQLdb


class DbHandler(object):

    def __init__(self, **db_config):
        self.db_config = db_config
        self.conn = None
        self.connect()

    def connect(self):
        autocommit = self.db_config.get("autocommit", True)
        database = self.db_config.get('database', 'test')
        self.conn = MySQLdb.connect(
            host=self.db_config.get('host', 'localhost'),
            port=self.db_config.get('port', 3306),
            user=self.db_config.get('user', 'root'),
            passwd=self.db_config.get('password', ''),
            db=database,
            charset=self.db_config.get('charset', 'utf8'),
            autocommit=autocommit
        )
        self.conn.select_db(database)

    def get_conn(self):
        if not self.conn or not self.conn.open:
            self.connect()
        try:
            self.conn.ping()
        except MySQLdb.OperationalError:
            self.connect()
        return self.conn

    def execute(self, *args):
        cursor = self.get_conn().cursor()
        cursor.execute(*args)
        return cursor

    def __del__(self):
        if self.conn and self.conn.open:
            self.conn.close()


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
