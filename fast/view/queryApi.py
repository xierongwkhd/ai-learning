import re
from enum import Enum
from typing import List, Any, Self

from fastapi import APIRouter
from fastapi import Query
from fastapi.params import Body
from pydantic import BaseModel, Field, field_validator

query = APIRouter(prefix='/query', tags=['查询模块'])

@query.get('/query-all', summary='查询所有数据')
async def query_all():
    print('查询')
    return {'msg': '列表'}

class User(BaseModel):
    userId: str = Field(max_length=10, min_length=10, decription='用户ID')
    userName: str = Field(max_length=3, min_length=2, decription = '用户名称')
    orgId: int = Field(default=0, description='用户机构')

    @field_validator('userId')
    def validate(cls, value):
        assert not (re.match(r'^\d{10}$', value)) is None
        return value

@query.get('/queryById/{id}', summary='查询单笔数据')
async def query_all(id: int):
    print(f'查询{id}')
    return

class UPDATE_NAME(Enum):
    user1 = '用户1'
    user2 = '用户2'

@query.put('/updateByName/{name}', summary='更新单笔数据')
async def updateByName(name: UPDATE_NAME):
    print(f'更新name{name.name}')
    print(f'更新value{name.value}')
    return {'msg': name}

@query.post('/updateUserInfo', summary='更新用户信息')
async def updateByName(user: User):
    print(f'更新userId{user.userId}')
    print(f'更新userName{user.userName}')
    print(f'更新orgId{user.orgId}')
    return {'msg': user}

@query.post('/updateUserNameById', summary='更新用户信息')
async def updateByName(userId: str = Body(default=None, description='用户ID'),
                       userName: str = Body(default=None, description='用户名称')):
    if userId is not None:
        print(f'更新userId{userId}')
    if userName is not None:
        print(f'更新userName{userName}')
    return {'msg': 'ok'}

@query.get('/queryByCondition', summary='条件查询')
async def updateByName(id: str = Query(default=None, max_length= 10, min_length=10, regex=r'^\d{10}$', description='用户ID'),
                       name: str = Query(default=None, decription='用户名称')):
    print(id)
    print(name)
    return {'msg': 'ok'}

@query.delete('/batchDeleteByIds', summary='批量删除')
async def query_all(ids: List[int] = Query(default=[], description='用户ID列表')):
    print(ids)
    return {'msg': ids}

