import os
import json

result_path = "/mnt/beeyan/REVERIE/tasks/REVERIE/experiments/releaseCheck/results/NP_cg_pm_sample_imagenet_mean_pooled_1heads_val_unseen.json"

data_path = "/mnt/beeyan/REVERIE/tasks/REVERIE/data/REVERIE_val_unseen.json"


print("server is listening")


print("server rpc begin")


# return all the picture id
def func(instruction_id):

    # 1. open the data_path json file

    # 2. look up the json file and find the instruction_id

    # 3. get the scan id

    # 4. look up the result_path json file and find the trajectory list

    # 5. according to the trajectory list #4 and the scanid #3 to look up the picture

    #1 
    with open(data_path) as data_json_file:
        data_json = json.load(data_json_file)
        print(data_json)


func(211_3)


