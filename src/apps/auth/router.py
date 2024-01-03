# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2023/12/26 21:24
"""
import uuid

from fastapi import APIRouter

from src.ext import cache
from src.apps.auth import models
from src.apps.auth import schemas
from src.response import Response
from src.exceptions import GenericException

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
async def login(schema: schemas.LoginSchema):
    user = await models.User.filter(username=schema.username).first()
    if not user:
        raise GenericException(msg="用户不存在")

    if not user.verify_password(schema.password):
        raise GenericException(msg="密码错误")

    token = uuid.uuid4().hex
    await cache.set(token, value=user.username)
    return Response(data={"token": token}, msg="登录成功")


@router.post("/register")
async def register(schema: schemas.RegisterSchema):
    user = models.User(username=schema.username)
    user.make_password(schema.password)
    await user.save()

    return Response(msg="注册成功")


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
