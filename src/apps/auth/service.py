# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2023/12/26 21:45
"""


class AuthService:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.user = None

    def exists(self) -> bool:
        if self.username:
            return True

        return False
