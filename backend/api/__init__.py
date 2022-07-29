# -*- coding: utf-8 -*-
# @Time    : 2022/7/22 14:02
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : __init__.py.py
# @Software: PyCharm
import asyncio

import aioredis as aioredis
from aioredis import Redis
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi import FastAPI, applications
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from .v1 import v1
from backend.core import config

app = FastAPI(
    description=config.core_settings.DESC,
    title=config.core_settings.TITLE,
)

app.include_router(v1, prefix="/api")


# 解决swagger文档加载不出来的问题
def swagger_monkey_patch(*args, **kwargs):
    return get_swagger_ui_html(
        *args, **kwargs,
        swagger_js_url='https://cdn.jsdelivr.net/npm/swagger-ui-dist@4/swagger-ui-bundle.js',
        swagger_css_url='https://cdn.jsdelivr.net/npm/swagger-ui-dist@4/swagger-ui.css'
    )


applications.get_swagger_ui_html = swagger_monkey_patch



async def init():
    user = 'root'
    password = 'admin*123'
    db_name = 'test'
    await Tortoise.init(
        # 指定mysql信息
        db_url=f'mysql://{user}:{password}@127.0.0.1:3306/{db_name}',
        # 指定models
        modules={'models': ['backend.models']}
    )
    # 按照模型生成表
    # await Tortoise.generate_schemas()


# core跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.core_settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
asyncio.run(init())
