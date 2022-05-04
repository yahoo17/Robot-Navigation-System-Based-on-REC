from agileutil.rpc.server import TcpRpcServer, rpc
import asyncio

@rpc
class TestService:

    def hello(self, name):
        return "Hello, {}!".format(name)

    async def add(self, a, b, c):
        asyncio.sleep(1)
        return a + b + c

@rpc
def hello(name):
    return "Hello, {}!".format(name)

server = TcpRpcServer('0.0.0.0', 2061)
server.serve()

