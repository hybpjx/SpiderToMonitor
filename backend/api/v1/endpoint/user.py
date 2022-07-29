# -*- coding: utf-8 -*-
# @Time    : 2022/7/25 16:32
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : user.py
# @Software: PyCharm
from fastapi import APIRouter, Depends, HTTPException
from fastapi_amis_admin.amis import Status
from tortoise.contrib.fastapi import HTTPNotFoundError

from backend.core import deps
from backend.models import Users
from backend.schemas import (
    UserIn_Pydantic,
    User_Pydantic,
    Response200,
    Response400,
)

user = APIRouter(tags=['用户相关'], dependencies=[Depends(deps.get_current_user)])


@user.get("/user", summary="当前用户")
async def current_user(user_obj: Users = Depends(deps.get_current_user)):
    return await User_Pydantic.from_tortoise_orm(user_obj)


@user.put("/user", summary="修改信息")
async def user_update(user_form: UserIn_Pydantic, user_obj: Users = Depends(deps.get_current_user)):
    """
    修改当前用户信息
    """
    user_form.username = user_obj.username
    user_form.password = user_obj.password
    if await Users.filter(username=user_obj.username).update(**user_form.dict()):
        return Response200(data=await User_Pydantic.from_tortoise_orm(user_obj))
    return Response400(msg="更新失败")


@user.delete("/user/{user_id}", response_model=Status, responses={404: {"model": HTTPNotFoundError}})
async def delete_user(user_id: int):
    deleted_count = await Users.filter(id=user_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return Status(message=f"Deleted user {user_id}")


# 指定能导出去的包
__all__ = [
    "user"
]
