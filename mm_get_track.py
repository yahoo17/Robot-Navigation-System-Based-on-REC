import os
import json
import compose
result_path = "/mnt/beeyan/REVERIE/tasks/REVERIE/experiments/releaseCheck/results/NP_cg_pm_sample_imagenet_mean_pooled_1heads_val_unseen.json"

data_path = "/mnt/beeyan/REVERIE/tasks/REVERIE/data/REVERIE_val_unseen.json"

# data_set_path = "/mnt/beeyan/Matterport/v1/scans"

# data_set_path = "/home/cike/REVERIE/Matterport/v1/scans"


print("server is listening")


print("server rpc begin")


# return all the picture id
def func(instruction_id):

    # 1. open the data_path json file

    # 2. look up the json file and find the instruction_id

    # 3. get the scan id

    # 4. look up the result_path json file and find the trajectory list

    # 5. according to the trajectory list #4 and the scanid #3 to look up the picture
    print("get_track begin")
    print("#1 #2 #3")

    scan = "random"
    instruction_id = instruction_id.strip()
    with open(data_path) as data_json_file:
        data_json = json.load(data_json_file)
        for single_task in data_json:
            # print(single_task["id"])

            if single_task["id"] == instruction_id:
                scan = single_task["scan"]
                print("got the scan: "+ scan)
    
    print("#4")
    trajectory = []
    sub_instrution = instruction_id + "_0"
    with open(result_path) as result_json_file:
        result_json = json.load(result_json_file)
        for single_task in result_json:
            if single_task["instr_id"] == sub_instrution:
                trajectory = single_task["trajectory"]
                print("get the trajectory")
                print(trajectory)
    
    # zsNo4HB9uLZ
    print("#5")
    data_set_path = "/home/cike/REVERIE/Matterport/v1/scans/" + scan + "/matterport_color_images/"
    # data_set_path = "/mnt/beeyan/Matterport/v1/scans/zsNo4HB9uLZ/zsNo4HB9uLZ/matterport_color_images/"

    image_path_list = []
    for node in trajectory:
        viewpointid = node[0]
        compose.image_compose(data_set_path ,viewpointid)
        # print(viewpointid)
        image_path = data_set_path + viewpointid + "_i0_0.jpg"
        image_path = data_set_path + viewpointid + "_final.jpg"
        print(image_path)
        image_path_list.append(image_path)

    print("get_track, image path list size:" + str(len(image_path_list)))
    return image_path_list

    
            
            
# def main_server(image_path_list):
#     # server
#     import socket               # 导入 socket 模块
#
#     s = socket.socket()         # 创建 socket 对象
#     host = socket.gethostname()  # 获取本地主机名
#     port = 12345                # 设置端口
#     s.bind((host, port))        # 绑定端口
#
#     s.listen(5)                 # 等待客户端连接
#     while True:
#         conn, addr = s.accept()     # 建立客户端连接
#         print('连接地址:', addr)
#         for pic_path in image_path_list:
#             with open(pic_path, 'rb') as f:
#                 data = f.read()
#                 conn.send(str(len(data)).encode('utf-8'))
#                 conn.send(data)
#         conn.close()                # 关闭连接
    
    
        
#
# if __name__ == "__main__":
#     func("4634_215")



