# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2024/1/7 22:11
"""
from socketio import AsyncServer, ASGIApp

sio = AsyncServer(async_mode='asgi', cors_allowed_origins="*")
asgi_app = ASGIApp(sio, socketio_path="websocket/v1")


@sio.event
async def connect(sid: str, environ: dict, auth):
    print("sid", sid)
    print("environ", environ)
    print("auth", auth)


@sio.event
async def disconnect(sid: str):
    print("disconnect", sid)
