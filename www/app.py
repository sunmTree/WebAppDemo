#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SunTree'

import logging; logging.basicConfig(level=logging.INFO)
import asyncio
from aiohttp import web


async def index(request):
    return web.Response(body=b'<h1>Hello, Web App</h1>', content_type='text/html')


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('Start server for 127.0.0.1:9000')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()      # 针对并发

