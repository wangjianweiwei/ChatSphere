# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2023/12/26 21:21
"""
from fastapi import FastAPI

from src.ext import extend
from src.response import Response
from src.exceptions import GenericException

app = FastAPI(lifespan=extend)


@app.exception_handler(GenericException)
async def generic_exception_handle(request, ex: GenericException):
    return Response(**ex.__dict__)
