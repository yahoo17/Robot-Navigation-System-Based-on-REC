import PIL.Image as Image
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os
import cv2
def bbox2(IMAGES_PATH,viewpointid):
    # [
    #     486,
    #     324,
    #     154,
    #     156
    # ],
    class_name = "towel"
    # b_box 左上角坐标
    ptLeftTop = np.array([486, 324])
    # 文本框左上角坐标
    textleftop = []
    # b_box 右下角坐标
    ptRightBottom = np.array([154+486, 156+324])
    # 框的颜色
    point_color = (0, 255, 0)
    # 线的厚度
    thickness = 2
    # 线的类型
    lineType = 4

    # (500, 375, 3) -> h w c
    src = cv2.imread(IMAGES_PATH + viewpointid+"_i0"+"_0"+".jpg")
    # cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
    src = np.array(src)
    # 画 b_box
    cv2.rectangle(src, tuple(ptLeftTop), tuple(ptRightBottom), point_color, thickness, lineType)

    # 获取文字区域框大小
    t_size = cv2.getTextSize(class_name, 1, cv2.FONT_HERSHEY_PLAIN, 1)[0]
    # 获取 文字区域右下角坐标
    textlbottom = ptLeftTop + np.array(list(t_size))
    # 绘制文字区域矩形框
    cv2.rectangle(src, tuple(ptLeftTop), tuple(textlbottom), point_color, -1)
    # 计算文字起始位置偏移
    ptLeftTop[1] = ptLeftTop[1] + (t_size[1] / 2 + 4)
    # 绘字
    cv2.putText(src, class_name, tuple(ptLeftTop), cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 0, 255), 1)
    # 打印图片的shape
    print(src.shape)

    # cv2.imshow('image', src)
    cv2.imwrite(IMAGES_PATH + viewpointid+"_i0"+"_0"+".jpg",src)
    cv2.waitKey(0)
    # cv2.destroyAllWindows()


# def bbox_process():
#     bbox_=  [
#         486,
#         324,
#         154,
#         156
#     ],
#
#     color_for_draw = tuple(np.random.randint(0, 255, size=[3]))
#
#     pre_image = from_image = Image.open(IMAGES_PATH + viewpointid+"_i0"+"_0"+".jpg" )
#
#     draw = ImageDraw.Draw(pre_image)
#     draw.rectangle([bbox_[0], bbox_[1], bbox_[2], bbox_[3]], outline=color_for_draw, width=2)


# 定义图像拼接函数
def image_compose(data_set_path, viewpointid):
    IMAGES_PATH = data_set_path  # 图片集地址
    IMAGES_FORMAT = ['.jpg', '.JPG']  # 图片格式
    IMAGE_SIZE = 256  # 每张小图片的大小
    IMAGE_ROW = 3  # 图片间隔，也就是合并成一张图后，一共有几行
    IMAGE_COLUMN = 6  # 图片间隔，也就是合并成一张图后，一共有几列
    # scanid = "0b22fa63d0f54a529c525afbf2e8bb25"
    IMAGE_SAVE_PATH = IMAGES_PATH + viewpointid + "_final.jpg"
    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_SIZE, IMAGE_ROW * IMAGE_SIZE)) #创建一个新图
    # 循环遍历，把每张图片按顺序粘贴到对应位置上

    bbox2(IMAGES_PATH,viewpointid)
    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            from_image = Image.open(IMAGES_PATH + viewpointid+"_i"+str(y-1)+"_"+str(x-1)+".jpg" ).resize(
                (320, 256), Image.ANTIALIAS)
            to_image.paste(from_image, ((x - 1) * IMAGE_SIZE, (y - 1) * IMAGE_SIZE))
    return to_image.save(IMAGE_SAVE_PATH) # 保存新图


# image_compose("0b22fa63d0f54a529c525afbf2e8bb25") #调用函数


