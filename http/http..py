import aiohttp
import asyncio


class HttpException(Exception):
    pass



class HttpSession:
    def __init__(self):
        self.session = aiohttp.ClientSession()
        self.methods = {
            'get': self.session.get,
            'post': self.session.post,
            'put': self.session.put,
            'delete': self.session.delete,
            'head': self.session.head,
            'options': self.session.options,
            'patch': self.session.patch
        }
    
    async def do(self, method, url, **kwargs):
        if method not in self.methods:
            raise HttpException('Invalid method')
        
        async with self.methods[method](url, **kwargs) as response:
            return await response.text()
