# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2023/12/26 21:21
"""
from fastapi import FastAPI
from src.apps import auth

app = FastAPI()

app.include_router(auth.router)
