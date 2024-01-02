# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2024/1/2 22:14
"""
from fastapi.responses import UJSONResponse

from src.codes import SUCCESS


class Response(UJSONResponse):

    def __init__(self, data: dict = None, code: int = SUCCESS, msg: str = 'OK', **kwargs):
        content = {"code": code, "data": data, "msg": msg}
        super().__init__(content, 200, **kwargs)
