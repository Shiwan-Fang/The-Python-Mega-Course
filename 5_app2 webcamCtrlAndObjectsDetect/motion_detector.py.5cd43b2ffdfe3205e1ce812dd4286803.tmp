# from distutils.command.build_scripts import first_line_re
import cv2
import time
import pandas
from datetime import datetime


first_frame = None
status_list = [None, None]
times = []
df = pandas.DataFrame(columns=["Start", "End"])


video = cv2.VideoCapture(0)  # 打开你的视频（路径），或者是摄像头（0），运行这个之后可以看到摄像头被激活了


while True:  # 一直是true，会一直运行

    check, frame = video.read()  # frame是摄像头捕捉到的图像（帧）
    status = 0

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 将摄像头捕捉到的图像转换成灰色
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    # 高斯滤波，图像处理中常用的滤波之一， (width,hight)
    # 对图像进行平滑的同时，同时能够更多的保留图像的总体灰度分布特征对图像进行平滑的同时，同时能够更多的保留图像的总体灰度分布特征

    if first_frame is None:
        first_frame = gray  # 得到激活摄像头之后的第一帧图片，可将其看作对照组？
        continue  # 回到while loop的起点，而不是运行下面的代码

    delta_frame = cv2.absdiff(first_frame, gray)
    # OpenCV 中计算两个数组差的绝对值的函数，即对照第一帧成像时哪些部分发生了变化
    # 图像是灰度的
    thresh_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    # 图像是黑白的 简单阈值当然是最简单，选取一个全局阈值，然后就把整幅图像分成了非黑即白的二值图像了，会得到一个元组
    thresh_frame = cv2.dilate(thresh_delta, None, iterations=2)
    # 膨胀函数，当分割出来的mask包含一些小“斑点”时，腐蚀操作可以去掉这些“斑点”；当分割图像轮廓不完整时，膨胀可以补全这些轮廓
    # 简单来说使黑白图像更清晰了

    (cnts, _) = cv2.findContours(thresh_frame.copy(),
                                 cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 轮廓检测，检测thresh_frame/只检测外轮廓/只存储水平，垂直，对角直线的起始点,将检测到的轮廓存储在一个元组中

    for contour in cnts:  # 如果我捕捉到的轮廓在1000像素以上，就用绿色的边框框住它
        if cv2.contourArea(contour) < 1000:
            continue  # 回到for loop的起点
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        # 获得一个图像的最小矩形边框一些信息，括号中的参数是一个二值图像，它可以返回四个参数
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
    status_list.append(status)

    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())

    cv2.imshow("capturing", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("threshole Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)  # 1/1000秒

    if key == ord('q'):  # 在键盘上点q，这个loop会结束
        if status == 1:
            times.append(datetime.now())
        break


print(status_list)
print(times)

for i in range(0, len(times), 2):  # 2是指i分别取0、3、5...
    df = df.append({"Start": times[i], "End": times[i+1]}, ignore_index=True)

df.to_csv("5_app2 webcamCtrlAndObjectsDetect\Times.csv")

video.release()


cv2.destroyAllWindows
