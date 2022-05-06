from agileutil.rpc.client import TcpRpcClient
import base64

def decode_picture(base64_data,file_name):
    file_name_tem = file_name + ".jpg"
    with open(file_name_tem, 'wb') as file:
        jiema = base64.b64decode(base64_data)  # 解码
        file.write(jiema)  # 将解码得到的数据写入到图片中

cli = TcpRpcClient('127.0.0.1', 2061, timeout = 2)


resp = cli.call('TestService.add', a=1, b=2, c=3)
print(resp)

# resp = cli.call('TestService.hello', name = 'xiaoming')
# print(resp)

def get_image(instruction_id):
    resp = cli.call('TestService.get_image_list', instruction_id= instruction_id)
    # print(resp)
    for index, file in enumerate(resp):
        decode_picture(file,str(index))
    return len(resp), resp

