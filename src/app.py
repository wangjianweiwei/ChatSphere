# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2023/12/26 21:21
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.ext import extend
from src.http import Response, GenericException

app = FastAPI(lifespan=extend)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(GenericException)
async def generic_exception_handle(request, ex: GenericException):
    return Response(**ex.__dict__)
