# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2024/1/2 22:46
"""
from enum import Enum, unique
from dataclasses import dataclass


@dataclass
class Code:
    code: int
    msg: str


@unique
class Codes(Enum):
    # 通用
    success = Code(2000, "Success")
    error = Code(5000, "Error")
    # auth
    account_invalid = Code(6001, "账户无效")
    password_error = Code(6002, "密码错误")
    # chat
