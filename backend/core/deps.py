# -*- coding: utf-8 -*-
# @Time    : 2022/7/25 16:56
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : deps.py
# @Software: PyCharm
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi import status
from jose import jwt, JWTError
from starlette.requests import Request

from backend.core import config
from backend.models import Users

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/user/info")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, config.core_settings.SECRET_KEY, algorithms=[config.core_settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await Users.get(username=username)
    if user is None:
        raise credentials_exception
    return user
