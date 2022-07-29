# -*- coding: utf-8 -*-
# @Time    : 2022/7/22 14:04
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : config.py
# @Software: PyCharm


from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    TITLE: Optional[str] = "爬虫列表"

    DESC: Optional[str] = """
    - tortoise —— fastapi
    """

    # JWT 安全配置项目
    SECRET_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 3

    ORIGINS = [
        "http://localhost.com:3000",
        "https://127.0.0.1:3000",
        "http://localhost",
        "http://localhost:5000",
    ]


core_settings = Settings()
