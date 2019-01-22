import cv2
import numpy as np


def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width =image.shape[1]
    channels =image.shape[2]
    print('width: %s,height: %s,channels: %s'%(width,height,channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row,col,c]
                image[row,col,c]=255-pv
    cv2.imshow('pixels_demo',image)



src =cv2.imread('e:/cat.jpg')
new =cv2.resize(src,(0,0),fx=0.5,fy=0.5,interpolation=cv2.INTER_CUBIC)#对原图像进行缩小
cv2.namedWindow('cat')
cv2.imshow('cat',new)
t1 = cv2.getTickCount()#getTickCount()：用于返回从操作系统启动到当前所经的计时周期数
access_pixels(new)
t2 =cv2.getTickCount()
#getTickFrequency()：用于返回CPU的频率。这里的单位是秒，也就是一秒内重复的次数。
time =(t2-t1)/cv2.getTickFrequency();#总次数/一秒内重复的次数 = 时间(s)
print('time:%sms'%(time*1000))#1000 *总次数/一秒内重复的次数= 时间(ms)
cv2.waitKey(0)
cv2.destroyAllWindows()