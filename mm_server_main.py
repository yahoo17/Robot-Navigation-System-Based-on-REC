from agileutil.rpc.server import TcpRpcServer, rpc
from agileutil.rpc.server import HttpRpcServer, rpc
import asyncio
import mm_get_track

import base64

def encode_picture(img_path):
    with open(img_path, 'rb') as f:
        image_data = f.read()
        base64_data = base64.b64encode(image_data)  # base64编码
        return base64_data
        # print(base64_data)
        # print(type(base64_data))




@rpc
class TestService:

    def get_image_list(self, instruction_id):
        print("get_image_list begin")
        print("instruction_id"+instruction_id)
        image_path_list = mm_get_track.func(instruction_id)
        file_list = []
        for path in image_path_list:
            file = encode_picture(path)
            file_list.append(file)

        print("get_image_list, file_list size:" + str(len(file_list)))
        return file_list
        # return image_path_list


    def hello(self, name):
        return "Hello, {}!".format(name)

    async def add(self, a, b, c):
        asyncio.sleep(1)
        return a + b + c

# @rpc
# def hello(name):
#     return "Hello, {}!".format(name)


# server = TcpRpcServer('0.0.0.0', 2061)
# server.serve()


s = HttpRpcServer('0.0.0.0', 2061, workers=1)
s.serve()
