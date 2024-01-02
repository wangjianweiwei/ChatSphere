# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2023/12/26 21:26
"""


class GenericException(Exception):

    def __init__(self, code: int = 5000, data=None, msg: str = "error"):
        self.code = code
        self.data = data
        self.msg = msg
