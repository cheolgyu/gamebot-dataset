from datetime import datetime
import os

def gg_x1():
    # 창닫기
    path = "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_gotgl/ox_확대_수령0/"
    file_list = os.listdir(path)
    for file in file_list:
        if file.endswith(".jpg")  :
            arr = file.split(".")
            file_txt = path+arr[0]+".txt"
            if os.path.exists(file_txt):
                os.remove(file_txt)
            f = open(file_txt, 'w')
            data = "0 0.952344 0.779167 0.085938 0.130556\n \
                    4 0.419531 0.096528 0.106250 0.118056\n \
                    "
            f.write(data)
            f.close()            
def gg_x2():
    # 창닫기
    path = "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_gotgl/ox_확대_수령5x/"
    file_list = os.listdir(path)
    for file in file_list:
        if file.endswith(".jpg")  :
            arr = file.split(".")
            file_txt = path+arr[0]+".txt"
            if os.path.exists(file_txt):
                os.remove(file_txt)
            f = open(file_txt, 'w')
            data = "4 0.419531 0.096528 0.106250 0.118056\n "
            f.write(data)
            f.close()     
def gg_x3():
    # 창닫기
    path = "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_gotgl/ox_확대_수령50/"
    file_list = os.listdir(path)
    for file in file_list:
        if file.endswith(".jpg")  :
            arr = file.split(".")
            file_txt = path+arr[0]+".txt"
            if os.path.exists(file_txt):
                os.remove(file_txt)
            f = open(file_txt, 'w')
            data = "1 0.952344 0.779167 0.085938 0.130556\n \
                    4 0.419531 0.096528 0.106250 0.118056\n \
                    "
            f.write(data)
            f.close()    
def gg_x4():
    # 창닫기
    path = "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_gotgl/ox_확대_수령50_받기/"
    file_list = os.listdir(path)
    for file in file_list:
        if file.endswith(".jpg")  :
            arr = file.split(".")
            file_txt = path+arr[0]+".txt"
            if os.path.exists(file_txt):
                os.remove(file_txt)
            f = open(file_txt, 'w')
            data = "3 0.954687 0.762500 0.076563 0.138889\n \
                    1 0.886328 0.775000 0.088281 0.150000\n \
                    4 0.419531 0.096528 0.106250 0.118056\n \
                    "
            f.write(data)
            f.close()    


def gg_x5():
    # 창닫기
    path = "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_gotgl/ox_확대_수령x/"
    file_list = os.listdir(path)
    for file in file_list:
        if file.endswith(".jpg")  :
            arr = file.split(".")
            file_txt = path+arr[0]+".txt"
            if os.path.exists(file_txt):
                os.remove(file_txt)
            f = open(file_txt, 'w')
            data = "4 0.419531 0.096528 0.106250 0.118056\n \
                    "
            f.write(data)
            f.close()    


def gg_x6():
    # 창닫기
    path = "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_gotgl/ox_확대_수령x_받기/"
    file_list = os.listdir(path)
    for file in file_list:
        if file.endswith(".jpg")  :
            arr = file.split(".")
            file_txt = path+arr[0]+".txt"
            if os.path.exists(file_txt):
                os.remove(file_txt)
            f = open(file_txt, 'w')
            data = "3 0.954687 0.762500 0.076563 0.138889\n \
                    4 0.419531 0.096528 0.106250 0.118056\n \
                    "
            f.write(data)
            f.close()                
def gg_oo1():
    # 창닫기
    path = "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_gotgl/oo_확대_수령x_받기/"
    file_list = os.listdir(path)
    for file in file_list:
        if file.endswith(".jpg")  :
            arr = file.split(".")
            file_txt = path+arr[0]+".txt"
            if os.path.exists(file_txt):
                os.remove(file_txt)
            f = open(file_txt, 'w')
            data = "3 0.954687 0.762500 0.076563 0.138889\n \
                    4 0.419531 0.096528 0.106250 0.118056\n \
                    "
            f.write(data)
            f.close()    
def gg_oo2():
    # 창닫기
    path = "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_gotgl/oo_확대_수령0_받기/"
    file_list = os.listdir(path)
    for file in file_list:
        if file.endswith(".jpg")  :
            arr = file.split(".")
            file_txt = path+arr[0]+".txt"
            if os.path.exists(file_txt):
                os.remove(file_txt)
            f = open(file_txt, 'w')
            data = "3 0.954687 0.762500 0.076563 0.138889\n \
                    0 0.886328 0.775000 0.088281 0.150000\n \
                    4 0.419531 0.096528 0.106250 0.118056\n \
                    "
            f.write(data)
            f.close()    

def gg_oo3():
    # 창닫기
    path = "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_gotgl/oo_확대_수령0/"
    file_list = os.listdir(path)
    for file in file_list:
        if file.endswith(".jpg")  :
            arr = file.split(".")
            file_txt = path+arr[0]+".txt"
            if os.path.exists(file_txt):
                os.remove(file_txt)
            f = open(file_txt, 'w')
            data = "0 0.952344 0.779167 0.085938 0.130556\n \
                    4 0.419531 0.096528 0.106250 0.118056\n \
                    "
            f.write(data)
            f.close()    

def gg_1():
    # 창닫기
    path = "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_gotgl/확대_수령확인/"
    file_list = os.listdir(path)
    for file in file_list:
        if file.endswith(".jpg")  :
            arr = file.split(".")
            file_txt = path+arr[0]+".txt"
            if os.path.exists(file_txt):
                os.remove(file_txt)
            f = open(file_txt, 'w')
            data = "2 0.498437 0.804167 0.189063 0.094444\n \
                    "
            f.write(data)
            f.close()   
def gg_2():
    # 창닫기
    path = "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_gotgl/확대_창닫기/"
    file_list = os.listdir(path)
    for file in file_list:
        if file.endswith(".jpg")  :
            arr = file.split(".")
            file_txt = path+arr[0]+".txt"
            if os.path.exists(file_txt):
                os.remove(file_txt)
            f = open(file_txt, 'w')
            data = "10 0.967578 0.041667 0.044531 0.075000\n \
                    "
            f.write(data)
            f.close()               
gg_2()

# gg_v8()
# gg_v9()
# ee()          
#  rm ds/ds_gotgl/img/gotgl_video_2*
#  rm ds/ds_gotgl/img/gotgl_video_3*
#  rm ds/ds_gotgl/img/gotgl_video_4*
#  rm ds/ds_gotgl/img/gotgl_video_5*
# cp ds/ds_gotgl/수령_도움_할리스_독사진/* ds/ds_gotgl/img/
# cp ds/ds_gotgl/수령_확인/* ds/ds_gotgl/img/
# cp ds/ds_gotgl/식량_목재_석재_철과_음식_확대사진/* ds/ds_gotgl/img/
# cp ds/ds_gotgl/v8/* ds/ds_gotgl/img/
# cp ds/ds_gotgl/v9/* ds/ds_gotgl/img/
# cp ds/ds_gotgl/수령x_t1/* ds/ds_gotgl/img/
# cp ds/ds_gotgl/수령x_t2/* ds/ds_gotgl/img/
# ./yolo_mark ./ds/ds_gotgl/ox_확대_수령0 ./train.txt ./data.names
# ./yolo_mark ./ds/ds_gotgl/ox_확대_수령5x ./train.txt ./data.names
# ./yolo_mark ./ds/ds_gotgl/ox_확대_수령50 ./train.txt ./data.names
# ./yolo_mark ./ds/ds_gotgl/ox_확대_수령50_받기 ./train.txt ./data.names
# ./yolo_mark ./ds/ds_gotgl/ox_확대_수령x ./train.txt ./data.names
# ./yolo_mark ./ds/ds_gotgl/ox_확대_수령x_받기 ./train.txt ./data.names
# ./yolo_mark ./ds/ds_gotgl/oo_확대_수령x_받기 ./train.txt ./data.names < 14잔만함.
# ./yolo_mark ./ds/ds_gotgl/oo_확대_수령0_받기 ./train.txt ./data.names 빼자<- 이건: 라베링 개많음.120장
# ./yolo_mark ./ds/ds_gotgl/oo_확대_수령0 ./train.txt ./data.names