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
 # 알림창               
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

 # 상태바    
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
            data = "0 0.876562 0.782639 0.078125 0.112500\n"+"1 0.951172 0.765278 0.057031 0.102778\n"+"3 0.512109 0.085417 0.400781 0.159722\n"
            f.write(data)
            f.close()

dd()

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
            data = "0 0.876562 0.782639 0.078125 0.112500\n"+"1 0.951172 0.765278 0.057031 0.102778\n"+"3 0.512109 0.085417 0.400781 0.159722\n"
            f.write(data)
            f.close()
ee()            