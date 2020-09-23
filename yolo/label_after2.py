import os
from os.path import getsize
import random
import math


project="blackdesertm"
project_id="project_1"
ratio=0.1
img_path = "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_fivestars/img"
txt_path = "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_fivestars/img"
project_path = "/home/cheolgyu/workspace/gamebot/gamebot-yolo/workspace/fivestars/project_1"
project_train_file= project_path+"/train.txt"
project_valid_file= project_path+"/valid.txt"


txt_file_list = os.listdir(txt_path)

all_list=[]

for file in txt_file_list:
        
    if file.endswith(".txt") and getsize(txt_path+"/"+file) > 0 and file.find("netbook") == -1  and file != "classes.txt":
        file_name=file.split(".txt")
        chk_img = img_path+str("/"+file_name[0]+".jpg")
        if os.path.isfile(chk_img):
            all_list.append(str("/"+file_name[0]+".jpg"))
        else:
            os.remove(txt_path+"/"+file)
            
   
valid_list=[]
train_list=[]
all_cnt = len(all_list)
valid_cnt = math.ceil(ratio*all_cnt)

for i in range(int(valid_cnt)):
    idx = random.randint(0, len(all_list)-1)
    filename = all_list[idx]
    valid_list.append(filename)
    del all_list[idx]
for i in range(len(all_list)):
    filename = all_list[i]
    train_list.append(filename)

print ("end===================")
if os.path.isfile(project_train_file):
    os.remove(project_train_file)

if os.path.isfile(project_valid_file):
    os.remove(project_valid_file)

f = open(project_train_file, "w")
for filename in train_list:
    f.write(img_path+filename+"\n")
f.close()

f = open(project_valid_file, "w")
for filename in valid_list:
    f.write(img_path+filename+"\n")
f.close()