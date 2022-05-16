from agileutil.rpc.client import TcpRpcClient
from agileutil.rpc.client import HttpRpcClient
import base64

def decode_picture(base64_data,file_name):
    file_name_tem = file_name + ".jpg"
    with open(file_name_tem, 'wb') as file:
        jiema = base64.b64decode(base64_data)  # 解码
        file.write(jiema)  # 将解码得到的数据写入到图片中


# resp = cli.call('TestService.hello', name = 'xiaoming')
# print(resp)

def get_image(instruction_id):
    cli = TcpRpcClient('127.0.0.1', 2062, timeout=3)
    print("client rpc begin,instruction_id is "+instruction_id)
    resp = cli.call('TestService.get_image_list', instruction_id=instruction_id)
    print(resp)

    # test_conn()
    # c = HttpRpcClient('127.0.0.1', 2061)
    # resp = c.call('TestService.get_image_list', instruction_id)
    # print(resp)

    for index, file in enumerate(resp):
        decode_picture(file,str(index))
    return len(resp), resp

def test_conn():
    cli = TcpRpcClient('127.0.0.1', 2061, timeout=2)
    resp = cli.call('TestService.add', a=1, b=2, c=3)
    print(resp)

    # c = HttpRpcClient('127.0.0.1', 2061)
    # resp = c.call('TestService.add', 1,2,3)
    # print(resp)

# if __name__ == "__main__":
#     cli = TcpRpcClient('127.0.0.1', 2061, timeout=2)
#     resp = cli.call('TestService.add', a=1, b=2, c=3)
#     print(resp)
