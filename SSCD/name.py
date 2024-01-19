# -*- coding:utf-8 -*-
import glob

# imageList = glob.glob("/media/mym/My Passport/cj/MRI_data/GGZ202106/*/*/*/*")  # 图片所在文件夹的路径
imageList = glob.glob("./LEVIR/label/*")
imageList.sort()  #按照升序排序
f = open('./LEVIR/list/val.txt', 'a')  # 创建标签文件存放图片文件名
for item in imageList:

    # print(item)                                # images_test/m1_a_018_1.jpg
    img_name1 = item.split('/')[-1]  # 图片文件名018.jpg
    # img_name = img_name1.split('.')[0]
    print(img_name1)
    f.write(img_name1 + '\n')  # 将图片文件名逐行写入txt

print('OK')