# -*- coding: utf-8 -*-
# @Time    : 2022/7/22 14:05
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : MaintainedData.py
# @Software: PyCharm
from enum import Enum
from typing import List, Optional
from fastapi import APIRouter, HTTPException
from starlette import status
from tortoise.contrib.fastapi import HTTPNotFoundError

from backend.schemas.MaintainedData import MaintainedData_Pydantic, MaintainedDataIn_Pydantic
from backend.models.MaintainedData import MaintainedData
from backend.schemas.basic import Response404, Response200

data = APIRouter(tags=['数据模块'])


class order_byEnum(str, Enum):
    pear = ""
    banana = '-'


@data.get("/", summary="数据列表", response_model=List[MaintainedData_Pydantic])
async def data_list(
        order_by: order_byEnum = "",
        limit: int = 10,
        page: int = 1):
    #  limit 是显示的条数 ，page是页数
    skip = (page - 1) * limit
    return await MaintainedData_Pydantic.from_queryset(MaintainedData.all().offset(skip).limit(limit).order_by(
        f"{order_by}crawling_time"))


@data.post("/data", summary="新增数据", )
async def add_data(md_data: MaintainedData_Pydantic):
    movie_obj = await MaintainedData.create(**md_data.dict(exclude_unset=True))
    # movie_obj = await Movie.create(name="",year="",xx="")
    return await MaintainedData_Pydantic.from_tortoise_orm(movie_obj)


@data.put("/data/{data_id}", summary="编辑数据", responses={404: {"model": HTTPNotFoundError}})
async def update_data(site_id: str, md_data: MaintainedDataIn_Pydantic):
    updated_count = await MaintainedData.filter(site_id=site_id).update(**md_data.dict(exclude_unset=True))
    print(updated_count)
    if not updated_count:
        return Response404(msg=f"data {site_id} not found")
    return Response200(data=await MaintainedData_Pydantic.from_queryset_single(MaintainedData.get(site_id=site_id)))


@data.get("/data/{data_id}", summary="查找数据", response_model=MaintainedData_Pydantic,
          responses={404: {"model": HTTPNotFoundError}})
async def get_user(site_id: str):
    return await MaintainedData_Pydantic.from_queryset_single(MaintainedData.get(site_id=site_id))


@data.delete("/data/{data_id}", summary="删除数据", responses={404: {"model": HTTPNotFoundError}})
async def del_movie(site_id: str):
    deleted_count = await MaintainedData.filter(site_id=site_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"data {site_id} not found")
    return HTTPException(status_code=200, detail=f"Deleted Movie {site_id}")


@data.get("/filter/{run_computer}", summary=" 按照运行电脑查询")
async def queryDataByDataUser_name(run_computer: str,
                                   site_type: Optional[str] = None,
                                   limit: int = 10,
                                   page: int = 1,
                                   order_by: order_byEnum = "",
                                   ):
    skip = (page - 1) * limit
    origin_data = await MaintainedData_Pydantic.from_queryset(MaintainedData.filter(
        run_computer=run_computer,
        site_type=site_type,
    ).all().offset(
        skip).limit(
        limit).order_by(
        f"{order_by}crawling_time"))

    return HTTPException(status_code=status.HTTP_200_OK,
                         detail={"message": "请求成功", "data": origin_data})


@data.get("/all_computer", summary="获取所有运行电脑")
async def queryDataComputer_nameByData():
    run_computer = await MaintainedData.all().distinct().values("run_computer")
    if run_computer:
        return HTTPException(status_code=status.HTTP_200_OK,
                             detail={"message": "请求成功", "data": run_computer})

    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"message": "无数据内容"})


@data.get("/data_length", summary="获取长度")
async def queryDataLengthData_list():
    data_length = len(await MaintainedData.all().values())
    # print(data_length)
    return HTTPException(status_code=status.HTTP_200_OK,
                         detail={"message": "请求成功", "data": data_length})
