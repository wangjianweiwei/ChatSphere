# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2023/12/26 21:25
"""
import uuid
import secrets
from hashlib import md5

from tortoise import models, fields

from src.ext import cache


class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True, index=True)
    password = fields.CharField(max_length=128)
    password_hash = fields.CharField(max_length=128)
    create_at = fields.DatetimeField(auto_now_add=True)
    modify_at = fields.DatetimeField(auto_now=True)

    def make_password(self, password: str):
        self.password_hash = secrets.token_hex(8)
        obj = md5(self.password_hash.encode())
        obj.update(password.encode())
        self.password = obj.hexdigest()

    def verify_password(self, password: str) -> bool:
        obj = md5(self.password_hash.encode())
        obj.update(password.encode())

        return obj.hexdigest() == self.password

    async def login(self, expire: int) -> str:
        token = uuid.uuid4().hex
        await cache.set(token, value=self.username, ex=expire)

        return token

    @classmethod
    async def logout(cls, token) -> None:
        await cache.delete(token)
