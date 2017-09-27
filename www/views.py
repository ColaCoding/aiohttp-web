from aiohttp import web
import aiohttp_jinja2
from config import objects, database
from .models import User


async def index(request):
    return web.Response(text='Hello aiohttp!')


@aiohttp_jinja2.template('test.html')
async def test(request):
    # 渲染的数据
    context = {
        'msg': 'Hello aiohttp_jinja2 context!'
    }

    # 数据库操作
    p = await objects.get(User, username='hutzerg')
    # print(p.username, p.password)
    context['user'] = p
    return context


@aiohttp_jinja2.template('login.html')
async def login(request):
    pass


async def api_login(request):
    data = {
        'code': 11000,
        'msg': 'unknow'
    }
    post_data = await request.post()
    u, p = post_data.get('username', None), post_data.get('password', None)
    print(u, p)
    return web.json_response(data)
