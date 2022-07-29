# -*- coding: utf-8 -*-
# @Time    : 2022/7/22 14:05
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : __init__.py.py
# @Software: PyCharm
from fastapi import APIRouter
from .endpoint import *

v1 = APIRouter()

v1.include_router(data, prefix="/v1")
v1.include_router(login,prefix="/v1")
v1.include_router(user,prefix="/v1")
