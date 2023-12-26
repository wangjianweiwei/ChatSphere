# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2023/12/26 21:24
"""
from fastapi import APIRouter
from src.apps.auth.service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/login")
async def login():
    auth = AuthService()

    username = "admin"
    if not auth.check_username(username):
        return {"message": "用户名不存在"}



@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
