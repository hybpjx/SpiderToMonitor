# -*- coding: utf-8 -*-
# @Time    : 2022/7/22 14:15
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : MaintainedData.py
# @Software: PyCharm
from datetime import datetime
from typing import Optional, Iterable

from tortoise import fields, models, BaseDBAsyncClient


class MaintainedData(models.Model):
    """
    The User model
    """
    id = fields.SmallIntField(pk=True, index=True, description="ID", )
    site_id = fields.CharField(max_length=20, unique=True, description="网站ID")
    site_name = fields.CharField(max_length=128, null=False, description="网站名称")
    site_type = fields.CharField(max_length=16, null=False, description="网站类型")
    description = fields.CharField(max_length=255, default="",description="网站备注", )
    site_path_name = fields.CharField(max_length=128, null=True, description="目录名称")
    site_path_url = fields.CharField(max_length=128, null=True, description="目录链接")
    status = fields.CharField(max_length=128, null=True, description="脚本状态")
    run_computer = fields.CharField(max_length=255, null=True, description="运行电脑")
    run_directory = fields.CharField(max_length=255, null=True, description="运行目录")
    crawling_time :Optional[datetime]= fields.DatetimeField(auto_add=True, description="运行时间")
    err_message = fields.CharField(max_length=255, null=True, description="错误信息")


"""
 id: Optional[int] = Field(primary_key=True, title="ID")
    site_id: str = Field(max_length=32, title="网站ID")
    site_name: str = Field(max_length=255, title='网站名称')
    site_type: str = Field(max_length=32, title="网站类型")
    description: Optional[Text] = Field(default='', title='网站备注')
    site_path_name: str = Field(max_length=255, title="目录名称")
    site_path_url: Optional[AnyHttpUrl] = Field(title="目录链接")
    status: str = Field(max_length=32, title="脚本状态")
    run_computer: str = Field(max_length=255, title="运行电脑")
    run_directory: str = Field(max_length=255, title="运行目录")
    crawling_time: Optional[datetime] = Field(default="", title="运行时间")
    err_message: Optional[Text] = Field(title="错误信息")
"""
