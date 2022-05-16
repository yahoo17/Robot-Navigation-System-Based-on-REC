import PIL.Image as Image
import os
 

# 定义图像拼接函数
def image_compose(data_set_path, viewpointid):
    IMAGES_PATH = data_set_path  # 图片集地址
    IMAGES_FORMAT = ['.jpg', '.JPG']  # 图片格式
    IMAGE_SIZE = 256  # 每张小图片的大小
    IMAGE_ROW = 3  # 图片间隔，也就是合并成一张图后，一共有几行
    IMAGE_COLUMN = 6  # 图片间隔，也就是合并成一张图后，一共有几列
    # scanid = "0b22fa63d0f54a529c525afbf2e8bb25"
    IMAGE_SAVE_PATH = viewpointid + "_final.jpg"
    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_SIZE, IMAGE_ROW * IMAGE_SIZE)) #创建一个新图
    # 循环遍历，把每张图片按顺序粘贴到对应位置上
    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            from_image = Image.open(IMAGES_PATH + viewpointid+"_i"+str(y-1)+"_"+str(x-1)+".jpg" ).resize(
                (320, 256), Image.ANTIALIAS)
            to_image.paste(from_image, ((x - 1) * IMAGE_SIZE, (y - 1) * IMAGE_SIZE))
    return to_image.save(IMAGE_SAVE_PATH) # 保存新图


# image_compose("0b22fa63d0f54a529c525afbf2e8bb25") #调用函数


