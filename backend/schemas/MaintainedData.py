# -*- coding: utf-8 -*-
# @Time    : 2022/7/22 14:30
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : MaintainedData.py
# @Software: PyCharm
from tortoise.contrib.pydantic import pydantic_model_creator
from backend.models import MaintainedData

MaintainedData_Pydantic = pydantic_model_creator(MaintainedData, name="MaintainedData")
MaintainedDataIn_Pydantic = pydantic_model_creator(MaintainedData, name="MaintainedDataIn", exclude_readonly=True)
