#!/usr/bin/env python3

import asyncio
import async_timeout
from aiohttp import web
import sys
import os

SLEEP_TIME = 0.05


async def work():
    await asyncio.sleep(SLEEP_TIME)


async def sleep50(_):
    await work()
    return web.Response(text="")


async def hard_work(_):
    await work()
    await asyncio.gather(work(), work())
    try:
        async with async_timeout.timeout(SLEEP_TIME / 2):
            await work()
    except asyncio.TimeoutError:
        pass
    return web.Response(text="")


def get_app():
    app = web.Application()
    app.router.add_get('/sleep50', sleep50)
    app.router.add_get('/hard_work', hard_work)
    return app


if __name__ == "__main__":
    if len(sys.argv) > 1:
        import uvloop
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
        print('using uvloop')

    print(f'pid = {os.getppid()}')

    web.run_app(get_app(), port=8890)