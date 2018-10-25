#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# asyncio可以实现单线程并发IO操作 如何实现单线程并发IO。如果仅用在客户端，发挥的威力不大。如果把 asyncio 用在服务器端
# 例如web服务器，由于HTTP连接就是IO操作，因此可以用单线程 + coroutine 实现多用户的高并发支持
# 编写一个HTTP服务器分别处理如下URL

# / 首页返回 b'<h1>Index</h1>'
# /hello/{name} 根据URL参数返回文本 hello, %s!




