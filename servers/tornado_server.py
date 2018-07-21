#!/usr/bin/env python3
import os
import tornado.ioloop
import tornado.web
import tornado.gen
import tornado.util
from tornado.ioloop import IOLoop
import sys
import datetime

SLEEP_TIME = 0.05


@tornado.gen.coroutine
def old_work():
    yield tornado.gen.sleep(SLEEP_TIME)


class SimpleHandler(tornado.web.RequestHandler):
    async def get(self):
        await work()
        self.write('')


class OldStyleHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        yield old_work()
        self.write('')


async def work():
    await tornado.gen.sleep(SLEEP_TIME)


class HardWorkHandler(tornado.web.RequestHandler):
    timeout_time = datetime.timedelta(seconds=SLEEP_TIME / 2)
    async def get(self):
        await work()
        await tornado.gen.multi([work(), work()])
        try:
            await tornado.gen.with_timeout(self.timeout_time, work())
        except tornado.util.TimeoutError:
            pass


class HardWorkHandlerOldStyle(tornado.web.RequestHandler):
    timeout_time = datetime.timedelta(seconds=SLEEP_TIME / 2)

    @tornado.gen.coroutine
    def get(self):
        yield work()
        yield tornado.gen.multi([work(), work()])
        try:
            yield tornado.gen.with_timeout(self.timeout_time, work())
        except tornado.util.TimeoutError:
            pass


def make_app(uvloop=False):
    if uvloop:
        IOLoop.configure('tornado.platform.asyncio.AsyncIOLoop')
        import asyncio
        import uvloop
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    return tornado.web.Application([
        (r'/sleep50', SimpleHandler),
        (r'/oldstyle50', OldStyleHandler),
        (r'/hard_work', HardWorkHandler),
        (r'/hard_work_oldstyle', HardWorkHandlerOldStyle),
    ])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        app = make_app(uvloop=True)
    else:
        app = make_app(uvloop=False)

    print(f'pid = {os.getppid()}')
    app.listen(8890)
    tornado.ioloop.IOLoop.current().start()
