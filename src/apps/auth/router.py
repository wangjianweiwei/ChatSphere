# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2023/12/26 21:24
"""
from fastapi import APIRouter

from src.response import Response
from src.apps.auth.models import User
from src.exceptions import GenericException

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
async def login(username: str, password: str):
    user = await User.filter(username=username).first()
    if not user:
        raise GenericException(msg="用户不存在")

    if not user.check_password(password):
        raise GenericException(msg="密码错误")

    return Response(msg="登录成功")


@router.post("/register")
async def register(username: str, password: str):
    user = User(username=username)
    user.make_password(password)
    await user.save()

    return Response(msg="注册成功")


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
