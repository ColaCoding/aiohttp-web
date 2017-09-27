from . import views


def setup_routes(app):
    app.router.add_route('get', '/', views.index)
    app.router.add_route('*', '/login', views.login)
    app.router.add_route('*', '/api_login', views.api_login)
    app.router.add_route('get', '/test', views.test)
