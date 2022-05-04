from agileutil.rpc.client import TcpRpcClient

cli = TcpRpcClient('127.0.0.1', 2061, timeout = 2)
#cli = TcpRpcClient('202.38.247.165', 2061, timeout=2)

resp = cli.call('TestService.add', a=1, b=2, c=3)
print(resp)

resp = cli.call('hello', name = 'xiaoming')
print(resp)
