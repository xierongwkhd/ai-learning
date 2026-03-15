from fastapi import APIRouter

query = APIRouter(prefix='/query', tags=['查询模块'])

@query.get('/query-all', summary='查询所有数据')
async def query_all():
    print('查询')
    return {'msg': '列表'}