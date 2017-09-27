async def http_info(app, handler):
    async def middleware_handler(request):
        print(
            request.method,
            'HTTP', request.version[0], request.version[1],
            request.path,
        )
        return await handler(request)
    return middleware_handler