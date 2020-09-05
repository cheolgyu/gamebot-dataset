from datetime import datetime
import os

project_name="ds_baram"
path = "/home/cheolgyu/workspace/gamebot-dataset/ds/ds_baram/img/capture/all/"
file_list = os.listdir(path)
print(file_list)

def get_file_name():
    s = str(datetime.today().strftime("%Y_%m_%d_%H%M%S%f"))+".jpg"
    return s

def aa():
    for file in file_list:
        if file.endswith(".jpg") :
            new_filename=str(get_file_name())
            print(new_filename)
            os.rename(path+file,path+new_filename)
aa()            