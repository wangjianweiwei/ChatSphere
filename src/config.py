# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2023/12/26 21:21
"""
TIMEZONE = "Asia/Shanghai"

DATABASE = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.mysql',
            'credentials': {
                'host': 'localhost',
                'port': '3306',
                'user': 'root',
                'password': '123456',
                'database': 'ChatSphere',
            }
        }
    },
    'apps': {
        'models': {
            'models': ['aerich.models', 'src.apps.auth.models'],
            'default_connection': 'default',
        }
    },
    "timezone": TIMEZONE
}

CACHE = {
    "host": "localhost",
    "port": 9736,
    "password": "",
    "db": 0
}
