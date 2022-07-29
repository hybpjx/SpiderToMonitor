# -*- coding: utf-8 -*-
# @Time    : 2022/7/25 16:59
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : user.py
# @Software: PyCharm
from tortoise.contrib.pydantic import pydantic_model_creator
from backend.models import Users
User_Pydantic = pydantic_model_creator(Users, name="User", exclude=("password",))
UserIn_Pydantic = pydantic_model_creator(Users, name="UserIn", exclude_readonly=True)