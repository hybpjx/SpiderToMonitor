# -*- coding: utf-8 -*-
# @Time    : 2022/7/22 11:28
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : main.py
# @Software: PyCharm

from uvicorn import run
from api import app

if __name__ == '__main__':
    run("main:app", debug=True, reload=True)
