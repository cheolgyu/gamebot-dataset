from datetime import datetime
import os

project_name="ds_baram"
path = "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_gotgl/img/"
#file_list = os.listdir(path)
#print(file_list)

def get_file_name():
    s = str(datetime.today().strftime("%Y_%m_%d_%H%M%S%f"))+".jpg"
    return s

def aa():
    for file in file_list:
        if file.endswith(".jpg") :
            new_filename=str(get_file_name())
            print(new_filename)
            os.rename(path+file,path+new_filename)


def bb():
    for file in file_list:
        if file.endswith(".jpg") :
            arr = file.split(".")
            file_txt = path+arr[0]+".txt"
            if os.path.exists(file_txt):
                print(file_txt)
            else:
                f = open(file_txt, 'w')
                data = "0 0.876562 0.782639 0.078125 0.112500\n"+"1 0.951172 0.765278 0.057031 0.102778\n"
                f.write(data)
                f.close()
 # /img_3/ 수령확인     
path = "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_gotgl/img_3/"
#file_list = os.listdir(path)          
def cc():
    for file in file_list:
        if file.endswith(".jpg")  :
            arr = file.split(".")
            file_txt = path+arr[0]+".txt"
            if os.path.exists(file_txt):
                os.remove(file_txt)
            f = open(file_txt, 'w')
            data = "2 0.498437 0.804167 0.189063 0.094444\n"
            f.write(data)
            f.close()
#cc()
 # /img_2/ 수령+도움+상태바
path = "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_gotgl/img_2/"
#file_list = os.listdir(path)
def dd():
    for file in file_list:
        if file.endswith(".jpg")  :
            arr = file.split(".")
            file_txt = path+arr[0]+".txt"
            if os.path.exists(file_txt):
                os.remove(file_txt)
            f = open(file_txt, 'w')
            data = "0 0.876562 0.782639 0.078125 0.112500\n"+"1 0.951172 0.765278 0.057031 0.102778\n"+"3 0.392969 0.066667 0.032812 0.058333\n"
            f.write(data)
            f.close()

#dd()

 # /img/ 수령+도움+상태바
path = "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_gotgl/img/"
file_list = os.listdir(path)
def ee():
    for file in file_list:
        if file.endswith(".jpg")  :
            arr = file.split(".")
            file_txt = path+arr[0]+".txt"
            if os.path.exists(file_txt):
                os.remove(file_txt)
            f = open(file_txt, 'w')
            data = "0 0.876562 0.782639 0.078125 0.112500\n"+"1 0.951172 0.765278 0.057031 0.102778\n"+"3 0.392969 0.066667 0.032812 0.058333\n"
            f.write(data)
            f.close()
#ee()

# 카메라 가장높게+ 식량+목재+....+상태바+수령   

def gg_v8():
    path = "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_gotgl/v8/"
    file_list = os.listdir(path)
    for file in file_list:
        if file.endswith(".jpg")  :
            arr = file.split(".")
            file_txt = path+arr[0]+".txt"
            if os.path.exists(file_txt):
                os.remove(file_txt)
            f = open(file_txt, 'w')
            data = "0 0.883203 0.802083 0.069531 0.073611\n"+\
                "1 0.955078 0.769444 0.061719 0.119444\n"+\
                "3 0.391797 0.068056 0.033594 0.052778\n"+\
                "4 0.757812 0.691667 0.037500 0.063889\n"+\
                "4 0.755469 0.765972 0.034375 0.059722\n"+\
                "4 0.702344 0.704861 0.034375 0.065278\n"+\
                "4 0.687500 0.747917 0.031250 0.059722\n"+\
                "4 0.843359 0.700000 0.033594 0.061111\n"+\
                "4 0.797266 0.723611 0.030469 0.058333\n"+\
                "4 0.623438 0.684722 0.035937 0.069444\n"+\
                "4 0.599609 0.772222 0.030469 0.061111\n"+\
                "4 0.541406 0.742361 0.035937 0.062500\n"+\
                "5 0.476562 0.725000 0.037500 0.055556\n"+\
                "5 0.499609 0.672917 0.035156 0.054167\n"+\
                "5 0.562891 0.671528 0.033594 0.054167\n"+\
                "5 0.432813 0.675000 0.032812 0.058333\n"+\
                "5 0.399219 0.720139 0.032812 0.062500\n"+\
                "5 0.415625 0.634028 0.032812 0.056944\n"+\
                "5 0.370703 0.675694 0.032031 0.054167\n"+\
                "5 0.357422 0.634722 0.028906 0.050000\n"+\
                "5 0.305859 0.629167 0.033594 0.058333\n"+\
                "5 0.282813 0.545833 0.029687 0.055556\n"+\
                "6 0.321875 0.517361 0.029687 0.062500\n"+\
                "6 0.296094 0.500694 0.031250 0.051389\n"+\
                "6 0.293750 0.448611 0.028125 0.050000\n"+\
                "6 0.271875 0.518750 0.029687 0.054167\n"+\
                "6 0.265625 0.486111 0.028125 0.047222\n"+\
                "6 0.237891 0.535417 0.028906 0.048611\n"+\
                "6 0.236328 0.505556 0.030469 0.050000\n"+\
                "6 0.225781 0.481944 0.031250 0.055556\n"+\
                "7 0.309375 0.443750 0.028125 0.054167\n"+\
                "7 0.325781 0.420833 0.031250 0.058333\n"+\
                "7 0.290234 0.415972 0.028906 0.045833\n"+\
                "7 0.255078 0.455556 0.028906 0.050000\n"+\
                "7 0.267578 0.437500 0.030469 0.050000\n"+\
                "8 0.107031 0.504167 0.031250 0.061111\n"+\
                "8 0.147656 0.496528 0.029687 0.048611\n"+\
                "8 0.165234 0.536806 0.033594 0.059722\n"+\
                "8 0.117188 0.543056 0.031250 0.052778\n"


            f.write(data)
            f.close()
# ff_t1()             


def gg_v9():
    # 창닫기
    path = "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_gotgl/v9/"
    file_list = os.listdir(path)
    for file in file_list:
        if file.endswith(".jpg")  :
            arr = file.split(".")
            file_txt = path+arr[0]+".txt"
            if os.path.exists(file_txt):
                os.remove(file_txt)
            f = open(file_txt, 'w')
            data = "9 0.967578 0.041667 0.044531 0.075000\n"
            f.write(data)
            f.close()
gg_v8()
#gg_v9()
            
#  rm ds/ds_gotgl/img/gotgl_video_2*
#  rm ds/ds_gotgl/img/gotgl_video_3*
#  rm ds/ds_gotgl/img/gotgl_video_4*
#  rm ds/ds_gotgl/img/gotgl_video_5*
# cp ds/ds_gotgl/img_2/* ds/ds_gotgl/img/
# cp ds/ds_gotgl/img_3/* ds/ds_gotgl/img/
# cp ds/ds_gotgl/img_4/* ds/ds_gotgl/img/
# ./yolo_mark ./ds/ds_gotgl/식량_목재_석재_철과_음식_확대사진/ ./train.txt ./data.names