# -*- coding: UTF-8 -*-
from tkinter import *
import time

import tkinter as tk
from PIL import Image, ImageTk
from itertools import count
import mm_rpc_client

from gif import Image, save

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
    n, resp = mm_rpc_client.get_image(msg)
    return n, resp

class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im, root):
        self.m_root = root
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            title_i = "第" + str(self.loc) + "导航轨迹"
            self.m_root.title(title_i)
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)



def main():

    def mapFunc(str):
        if str == '\n':
            return "empty"
        data = {}
        data["2204_355"] = "2204_355"
        data["1220_391"] = "1220_391"
        data["2804_336"] = "2804_336"
        data["Enter the dining room and pick up the objects on the table"] = "4634_215"
        data["Go to the lounge on level 1 with the fire extinguisher and push the rope around the table closer to the walls"] = "2853_310"
        if str.strip('\n') in data.keys():
            return data[ str.strip('\n')]
        else:
            return "no_match"
    def sendMsg():#发送消息
        strMsg = "我:" + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+ '\n'
        txtMsgList.insert(END, strMsg, 'greencolor')
        send = txtMsg.get('0.0', END) # 输入发送的信息

        txtMsgList.insert(END, send) # 显示
        txtMsg.delete('0.0', END)
        returnMsg(mapFunc(send))
        cancelMsg()

    def load_img(index,path):
        root = tk.Toplevel(app)
        title_i = "第"+str(index)+"个轨迹"
        root.title(title_i)
        paned = tk.PanedWindow(root)
        paned.pack(fill=tk.X, side=tk.LEFT)
        img = Image.open(path)
        paned.photo = ImageTk.PhotoImage(img.resize((400,600)))
        tk.Label(paned, image=paned.photo).grid(row=index, column=0)

    def show_0(n):
        imgs =[]
        for i in range(n):
            imgs.append(str(i)+".jpg")

        frames = []
        for fn in imgs:
            frames.append(Image.open(fn))
        print("frame size:"+ str(len(frames)))
        save(frames, 'final_track.gif', duration=1, unit="seconds", between="frames", loop=False)
        root = tk.Toplevel(app)
        title_i = "导航轨迹"
        root.title(title_i)

        lbl = ImageLabel(root)
        lbl.pack()
        lbl.load('final_track.gif', root)


    def returnMsg(send):
        n = 0
        # returnback = "网络未连接，请检查与服务器通信是否正常"
        if send == 'empty':
            returnback = '请不要输入空消息噢'
        elif send == "no_match":
            returnback = "未能正确理解您的指令，请检查是否有误"
        else:
            n,_ = get_response(send)
            print("picture counts:", n)
            show_0(n)
            if n != 0:
                returnback = "已经把该instruction的轨迹展示出来了！"

        strMsg = "机器人:" + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+ '\n'
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
    app.title('SCUT机器人导航系统')

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



if  __name__ == "__main__":
    # mm_rpc_client.test_conn()
    main()

#!/usr/bin/python3
# coding=utf-8




