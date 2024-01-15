# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2023/12/26 21:24
"""
from fastapi import APIRouter, Header

from src.apps.auth import models
from src.apps.auth import schemas
from src.http import Response, Codes, GenericException

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
async def login(schema: schemas.LoginSchema):
    user = await models.User.filter(username=schema.username).first()
    if not user:
        raise GenericException(Codes.account_invalid)

    if not user.verify_password(schema.password):
        raise GenericException(Codes.password_error)

    token = await user.login(expire=120)

    return Response(data={"token": token}, msg="登录成功")


@router.post("/register")
async def register(schema: schemas.RegisterSchema):
    user = models.User(username=schema.username)
    user.make_password(schema.password)
    await user.save()

    return Response(msg="注册成功")


@router.get("/logout")
async def logout(token: str = Header(None)):
    await models.User.logout(token)

    return Response(msg="退出登录成功")


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
