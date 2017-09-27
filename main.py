import os

from aiohttp import web
from www.routes import setup_routes
import aiohttp_jinja2
import jinja2

from config import BASE_DIR
from middlewares import http_info


# 创建服务器
app = web.Application(middlewares=[
    http_info,
])

# 模板路径
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

# 静态文件路径(部署时请用 Nginx)
app.router.add_static('/static/', path=os.path.join(BASE_DIR, 'static'), name='static')

# 路由安装
setup_routes(app)

# 启动信号
# app.on_startup.append(init_mysql)

# 关闭信号
# app.on_cleanup.append(close_pg)

# 启动服务器
web.run_app(app, host='127.0.0.1', port=8080)
