from tornado import gen
import tornado.web
import tornado.ioloop
from utils import feed
import sys


class MainHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        feed_name = "test"
        feed_name = feed.get_feed(2345)
        self.set_status(200)
        raise gen.Return(self.write({"sss": feed_name}))


def make_app():
    return tornado.web.Application([
        (r"/test", MainHandler),
    ])


if __name__ == "__main__":
    port = sys.argv[1]
    print(port)
    app = make_app()
    app.listen(int(port))
    tornado.ioloop.IOLoop.current().start()
