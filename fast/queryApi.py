from enum import Enum
from pathlib import Path

from fastapi import APIRouter

query = APIRouter(prefix='/query', tags=['查询模块'])

@query.get('/query-all', summary='查询所有数据')
async def query_all():
    print('查询')
    return {'msg': '列表'}


@query.get('/queryById/{id}', summary='查询单笔数据')
async def query_all(id: int):
    print(f'查询{id}')
    return {'msg': id}

class UPDATE_NAME(Enum):
    user1 = '用户1'
    user2 = '用户2'

@query.put('/updateByName/{name}', summary='更新单笔数据')
async def updateByName(name: UPDATE_NAME):
    print(f'更新name{name.name}')
    print(f'更新value{name.value}')
    return {'msg': name}