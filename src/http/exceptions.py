# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2023/12/26 21:26
"""
from src.http import Codes


class GenericException(Exception):
    default = Codes.error

    def __init__(self, code: Codes = None, data=None, msg: str = None):
        code = code or self.default
        self.code = code
        self.data = data
        self.msg = msg
