# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2023/12/26 21:25
"""
from pydantic import BaseModel


class LoginSchema(BaseModel):
    username: str
    password: str


class RegisterSchema(LoginSchema):
    pass
