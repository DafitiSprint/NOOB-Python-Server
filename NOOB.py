import tornado.ioloop
import tornado.web
from dispatcher import MethodDispatcher
from websocket import WebSocketHandler
from alert import AlertHandler

from tornado.options import define, options, parse_command_line

define("port", default=80, help="run on the given port", type=int)

app = tornado.web.Application([
    (r'/', WebSocketHandler),
    (r'/alert/.*', AlertHandler),
])

if __name__ == '__main__':
    parse_command_line()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()