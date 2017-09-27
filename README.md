# aiohttp web框架的练习代码
### 对python的asyncio, aiohttp异步库感兴趣，这是我的练习代码，使用后果自负
## 介绍
* 照着aiohttp官方文档一步步敲出来的示例代码，完美运行
* 使用peewee和peewee_async代替sqlalchemy及aiomysql，作为项目的框架的orm，和django一样优雅
* Mysql作为数据库，models.py已定义User模型，直接运行models.py文件即可创建mysql数据库表
## 环境依赖
* Python版本  
Python 3.5+  
* 依赖的第三方库  
```
pip install aiohttp
pip install aiohttp_jinja2
pip install aiomysql
pip install jinja2
pip install peewee
pip install peewee_async
```
* 运行  
`>>> python main.py`