import tornado.ioloop
import tornado.web
import os.path

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", jeni='a <strong>beautiful</strong> girl!')

application = tornado.web.Application([
    (r"/", MainHandler),
])

application.settings.update(dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
))

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
