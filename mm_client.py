# -*- coding: UTF-8 -*-
from tkinter import *
import time
import requests
import json

import mm_rpc_client

# import eval_release.py as eval_release
# def get_model_reply(msg):
#     instruction = msg
#     # (resfiles, split_tag, evalType='nav'):
#     # The easiest way to integrate into your project is to 
#     # preload all the objects bounding_box/label/visible_pos with the loadObjProposals() function 
#     # as in the eval_release.py file. 
#     # Then you are able to access visible objects using ScanID_Viewpoi

#     eval = eval_release.run_eval(resfiles, split_tag, evalType='nav')

def get_response(msg):
   
    n = mm_rpc_client.get_image(msg)

    return n

def main():


    def sendMsg():#发送消息
        strMsg = "我:" + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+ '\n'
        txtMsgList.insert(END, strMsg, 'greencolor')
        send = txtMsg.get('0.0', END) # 输入发送的信息
        txtMsgList.insert(END, send) # 显示
        txtMsg.delete('0.0', END)
        returnMsg(send)
        cancelMsg()

    def returnMsg(send):
        returnback = get_response(send)
        if send == '\n':
            returnback = '请不要输入空消息噢'
        strMsg = "华智冰:" + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+ '\n'
        txtMsgList.insert(END, strMsg, 'greencolor')
        txtMsgList.insert(END, returnback)
        txtMsgList.insert(END, '\n')
        txtMsg.delete('0.0', END)

    def cancelMsg():#取消信息
        txtMsg.delete('0.0', END)

    def sendMsgEvent(event):#发送消息事件
        if event.keysym =='Return':
            sendMsg()
    #创建窗口
    app = Tk()
    app.title('SCUT机器人——华智冰')

    #创建frame容器
    frmLT = Frame(width = 600, height = 360, bg = 'white')
    frmLC = Frame(width = 600, height = 160, bg = 'white')
    frmLB = Frame(width = 600, height = 30)
    frmRT = Frame(width = 500, height = 600)

    #创建控件
    txtMsgList = Text(frmLT)
    txtMsgList.tag_config('greencolor',foreground = '#008C00')#创建tag
    txtMsg = Text(frmLC)
    txtMsg.bind("<Return>", sendMsgEvent)
    btnSend = Button(frmLB, text = '发送', width = 8, command = sendMsg)
    btnCancel =Button(frmLB, text = '清空', width = 8, command = cancelMsg)
    imgInfo = PhotoImage(file = "background.png")
    lblImage = Label(frmRT, image = imgInfo)
    lblImage.image = imgInfo

    #窗口布局
    frmLT.grid(row = 0, column = 0, columnspan = 2, padx = 1, pady =3)
    frmLC.grid(row = 1, column = 0, columnspan = 2, padx = 1, pady = 3)
    frmLB.grid(row = 2, column = 0, columnspan = 2)
    frmRT.grid(row = 0, column = 2, rowspan = 3, padx =2, pady = 3)

    #固定大小
    frmLT.grid_propagate(0)
    frmLC.grid_propagate(0)
    frmLB.grid_propagate(0)
    frmRT.grid_propagate(0)

    btnSend.grid(row = 2, column = 0)
    btnCancel.grid(row = 2, column = 1)
    lblImage.grid()
    txtMsgList.grid()
    txtMsg.grid()

    #主事件循环
    app.mainloop()

def connect_to_server():
    import socket  # 导入 socket 模块
 
 
    s = socket.socket()  # 创建 socket 对象

    port = 12345  # 设置端口号
    
    s.connect(("202.38.247.165", port))
    r = s.recv(1024)
    print(r)
    data_len = eval(r)
    data = s.recv(data_len)
    s.close()
    
    
    with open(r'/Users/yahoo17/code/Robot-Navigation-System-Based-on-REC/a.jpg', 'ba') as f:
        f.write(data)
        f.close()


if  __name__ == "__main__":
    main()
