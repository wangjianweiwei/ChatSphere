# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2024/1/3 23:09
"""
import importlib
from typing import Union
from contextlib import asynccontextmanager

from fastapi import FastAPI
from redis.asyncio.client import Redis
from tortoise import Tortoise, connections

from src.config import DATABASE, CACHE, APPS

cache: Union[Redis, None] = None


def register_routers(app: FastAPI) -> None:
    for path in APPS:
        module = importlib.import_module(path)
        if router := getattr(module, "router", None):
            app.include_router(router)
        if asgi_app := getattr(module, "asgi_app", None):
            app.mount("", asgi_app)


async def startup(app) -> None:
    global cache
    # 初始化Redis
    cache = Redis(**CACHE)
    # 初始化MySQL
    await Tortoise.init(config=DATABASE)
    # 注册路由
    register_routers(app)


async def shutdown(app) -> None:
    await connections.close_all()
    await cache.aclose()


@asynccontextmanager
async def extend(app: FastAPI) -> None:
    await startup(app)

    yield

    await shutdown(app)
