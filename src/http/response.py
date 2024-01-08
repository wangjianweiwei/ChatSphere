# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2024/1/2 22:14
"""
from fastapi.responses import UJSONResponse

from src.http import Codes


class Response(UJSONResponse):

    def __init__(self, data: dict = None, code: Codes = Codes.success, msg: str = None, **kwargs):
        content = {"code": code.value.code, "data": data, "msg": msg if msg else code.value.msg}
        super().__init__(content, 200, **kwargs)
