from datetime import datetime
import os

project_name="ds_baram"
path = "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_gotgl/img_3/"
file_list = os.listdir(path)
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
file_list = os.listdir(path)          
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
file_list = os.listdir(path)
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
path = "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_gotgl/img_4/"
file_list = os.listdir(path)
def ff_t1():
    for file in file_list:
        if file.endswith(".jpg")  :
            arr = file.split(".")
            file_txt = path+arr[0]+".txt"
            if os.path.exists(file_txt):
                os.remove(file_txt)
            f = open(file_txt, 'w')
            data = "0 0.957031 0.776389 0.070312 0.125000\n"\
                    +"3 0.392969 0.066667 0.032812 0.058333\n"\
                    +"4 0.845703 0.700694 0.030469 0.062500\n"\
                    +"4 0.797656 0.724306 0.025000 0.059722\n"\
                    +"4 0.757422 0.694444 0.030469 0.061111\n"\
                    +"4 0.755078 0.757639 0.027344 0.056944\n"\
                    +"4 0.704687 0.709028 0.029687 0.062500\n"\
                    +"4 0.688672 0.747222 0.032031 0.066667\n"\
                    +"4 0.622656 0.687500 0.029687 0.072222\n"\
                    +"4 0.599219 0.771528 0.035937 0.062500\n"\
                    +"4 0.537500 0.740278 0.031250 0.069444\n"\
                    +"5 0.563281 0.670833 0.032812 0.063889\n"\
                    +"5 0.503125 0.664583 0.032812 0.059722\n"\
                    +"5 0.476953 0.721528 0.038281 0.070833\n"\
                    +"5 0.429297 0.669444 0.027344 0.069444\n"\
                    +"5 0.412891 0.631944 0.028906 0.063889\n"\
                    +"5 0.371094 0.672917 0.028125 0.065278\n"\
                    +"5 0.399609 0.715278 0.027344 0.063889\n"\
                    +"5 0.357422 0.635417 0.030469 0.062500\n"\
                    +"5 0.305078 0.621528 0.030469 0.059722\n"\
                    +"5 0.283203 0.543750 0.027344 0.068056\n"\
                    +"6 0.226172 0.479167 0.030469 0.047222\n"\
                    +"6 0.295312 0.493056 0.023438 0.044444\n"\
                    +"6 0.322266 0.515972 0.024219 0.051389\n"\
                    +"6 0.270312 0.517361 0.021875 0.048611\n"\
                    +"6 0.264844 0.493056 0.021875 0.052778\n"\
                    +"6 0.237109 0.500000 0.028906 0.050000\n"\
                    +"6 0.235547 0.538194 0.032031 0.056944\n"\
                    +"6 0.293750 0.447222 0.029687 0.058333\n"\
                    +"7 0.328125 0.427778 0.032812 0.066667\n"\
                    +"7 0.310156 0.445139 0.028125 0.054167\n"\
                    +"7 0.288672 0.417361 0.030469 0.048611\n"\
                    +"7 0.255859 0.456944 0.032031 0.058333\n"\
                    +"7 0.269141 0.434028 0.024219 0.054167\n"\
                    +"8 0.108984 0.500000 0.033594 0.058333\n"\
                    +"8 0.147266 0.494444 0.025781 0.050000\n"\
                    +"8 0.166016 0.534028 0.025781 0.059722\n"\
                    +"8 0.117188 0.545833 0.031250 0.052778\n"

            f.write(data)
            f.close()
ff_t1()              
     
            
#  rm ds/ds_gotgl/img/gotgl_video_2*
#  rm ds/ds_gotgl/img/gotgl_video_3*
#  rm ds/ds_gotgl/img/gotgl_video_4*
#  rm ds/ds_gotgl/img/gotgl_video_5*
# cp ds/ds_gotgl/img_2/* ds/ds_gotgl/img/
# cp ds/ds_gotgl/img_3/* ds/ds_gotgl/img/
# cp ds/ds_gotgl/img_4/* ds/ds_gotgl/img/
# ./yolo_mark ./ds/ds_gotgl/img_4/ ./train.txt ./data.names