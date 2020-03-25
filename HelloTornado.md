#  Hello Tornado

```python
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
```



<img src="C:\Users\Administrator\Desktop\666\2020.3.23\QQ截图20200325223108.png" style="zoom:200%;" />