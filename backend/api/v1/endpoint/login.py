# -*- coding: utf-8 -*-
# @Time    : 2022/7/25 16:34
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : login.py
# @Software: PyCharm
from datetime import timedelta

import aioredis
import tortoise
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.requests import Request
from fastapi.responses import Response

from backend.models import Users
from backend.core import verify_password, create_access_token, config, deps
from backend.schemas import (
    UserIn_Pydantic,
    User_Pydantic,
    Response200,
    Response400,
    Response404,
    ResponseToken,
    Response401,
    Response201
)

login = APIRouter(tags=['认证相关'])


@login.post("/user/login", summary="登录")
async def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        user = await Users.get(username=form_data.username)
    except tortoise.exceptions.DoesNotExist:
        return Response404()
    if verify_password(form_data.password, user.password):
        if verify_password(form_data.password, user.password):
            access_token_expires = timedelta(minutes=config.core_settings.ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = create_access_token(
                {"sub": user.username}, expires_delta=access_token_expires
            )
            return ResponseToken(access_token=access_token, token_type="bearer")
        return Response401()
    else:
        return Response400()


@login.put("/user/logout", summary="注销", )
async def user_logout(response: Response, user: Users = Depends(deps.get_current_user)):
    response.delete_cookie(user.username)
    return Response200()


@login.post("/user/register", summary="用户新增")
async def register(user: UserIn_Pydantic):
    if await Users.filter(username=user.username):
        return Response400(msg="用户已存在")
    return Response201(data=await User_Pydantic.from_tortoise_orm(await Users.create(**user.dict())))
