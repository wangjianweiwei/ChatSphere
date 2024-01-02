# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2023/12/26 21:21
"""
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from src.apps import auth
from src.config import DATABASE
from src.response import Response
from src.exceptions import GenericException

app = FastAPI()


@app.exception_handler(GenericException)
async def generic_exception_handle(request, ex: GenericException):
    return Response(**ex.__dict__)


app.include_router(auth.router)
register_tortoise(app, config=DATABASE, add_exception_handlers=True)
