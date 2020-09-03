import os
from os.path import getsize
import random
import math


project="baram_crop"
ratio=0.1
path = "./"+project+"/img/"
train_str="ds/"+project+"/img/"
valid_str="ds/"+project+"/img/"
train_txt="./"+project+"/train.txt"
valid_txt="./"+project+"/valid.txt"

dir_list = os.listdir(path)
print ("file_list: {}".format(dir_list))

classes=79
cat_list=[]

for i in range(classes):
    cat_list.append([])

at_list=[]
print ("cat_list size:"+str(len(cat_list)))
all_cnt=0

for dir in dir_list:
    if dir == "all" :
        
        path_dir=path+dir+"/"
        file_list = os.listdir(path_dir)
        
        for file in file_list:
            if file.endswith(".txt") and getsize(path_dir+file) > 0 and file.find("netbook") == -1  and file != "classes.txt":
                print ("size::"+str(getsize(path_dir+file)))
                print ("f::"+str(path_dir+file))
                file_name=file.split(".txt")
                f_filename = file_name[0]+".jpg"
                at_list.append(f_filename)

                f = open(path_dir+file, 'r')
                line = f.readline()
                d = line.split(" ")
                print(line.split(" "))
                class_id = d[0]
                f.close()
                cat_list[int(class_id)].append(dir+"/"+f_filename)
                all_cnt=all_cnt+1


file_str = ""
all_valid_list=[]
all_train_list=[]
print ("클래스별 갯수===================")
for class_id, class_list in enumerate(cat_list):
    if len(class_list) > 0:
        file_str = file_str+"\n" +str(class_id)+": {}".format(class_list)
        valid_list=[]
        train_list=[]
        tmp_list = class_list.copy()
        class_cnt = len(tmp_list)
        valid_cnt = math.ceil(ratio*class_cnt)
        for i in range(int(valid_cnt)):
            idx = random.randint(0, len(tmp_list)-1)
            filename = tmp_list[idx]
            valid_list.append(filename)
            del tmp_list[idx]
        for i in range(len(tmp_list)):
            filename = tmp_list[i]
            train_list.append(filename)
        cnt = len(valid_list)+len(train_list)
        print ("id :"+str(class_id)+" - a:"+str(len(cat_list))+"-c:"+str(len(class_list))+"-tr:"+str(len(train_list))+"-va:"+str(len(valid_list))+"     ="+str(cnt))
        all_valid_list = all_valid_list + valid_list
        all_train_list = all_train_list + train_list

#print ("->a:"+str(all_cnt)+"-tr:"+str(len(all_train_list))+"-va:"+str(len(all_valid_list))+"     ="+str(cnt))

print(file_str)
print ("파일생성===================")
if os.path.isfile(train_txt):
    os.remove(train_txt)

if os.path.isfile(valid_txt):
    os.remove(valid_txt)

f = open(train_txt, "w")
for filename in all_train_list:
    f.write(train_str+filename+"\n")
f.close()

f = open(valid_txt, "w")
for filename in all_valid_list:
    f.write(valid_str+filename+"\n")
f.close()