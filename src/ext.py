# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2024/1/3 23:09
"""
from typing import Union
from contextlib import asynccontextmanager

from fastapi import FastAPI
from redis.asyncio.client import Redis
from tortoise import Tortoise, connections

from src.config import DATABASE, CACHE

cache: Union[Redis, None] = None


def register_routers(app: FastAPI) -> None:
    from src.apps import auth
    app.include_router(auth.router)


@asynccontextmanager
async def extend(app: FastAPI) -> None:
    global cache

    cache = Redis(**CACHE)
    await Tortoise.init(config=DATABASE)
    register_routers(app)

    yield

    await connections.close_all()
    await cache.aclose()
