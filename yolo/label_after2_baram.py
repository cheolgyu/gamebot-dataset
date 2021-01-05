import os
from os.path import getsize
import random
import math



# 한폴더에 모든 이미지 짱박아 놓고 사용하기 보단 
# 스크린별로 분류해 폴더로 저장후에 
# project_1/1~7 수동으로 바꾸면서 valid.txt 업데이트 시키기 
# open a모드(파일 내용 추가)로 되어있는지 보기  
project="baram"
project_id="p1"
ratio=0.1
img_path = "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_baram/p1/"
txt_path = "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_baram/p1/"
project_path = "/home/cheolgyu/workspace/gamebot/gamebot-yolo/workspace/baram/p1"
project_train_file= project_path+"/train.txt"
project_valid_file= project_path+"/valid.txt"
dir_list=["baram_001","baram_0010","baram_0011","baram_002","baram_003","baram_004","baram_005","baram_006","baram_007","baram_008","baram_009"]

def one_dir(inp_img_path,inp_txt_path):
    print(inp_txt_path)
    txt_file_list = os.listdir(inp_txt_path)

    all_list=[]

    for file in txt_file_list:
            
        if file.endswith(".txt") and getsize(inp_txt_path+"/"+file) > 0 and file.find("netbook") == -1  and file != "classes.txt":
            file_name=file.split(".txt")
            chk_img = inp_img_path+str("/"+file_name[0]+".jpg")
            if os.path.isfile(chk_img):
                all_list.append(str("/"+file_name[0]+".jpg"))
            else:
                os.remove(inp_txt_path+"/"+file)
                
    
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
        #os.remove(project_train_file)
        print ("project_train_file===================")

    if os.path.isfile(project_valid_file):
        #os.remove(project_valid_file)
        print ("project_valid_file===================")

    f = open(project_train_file, "a")
    for filename in train_list:
        f.write(inp_img_path+filename+"\n")
    f.close()

    f = open(project_valid_file, "a")
    for filename in valid_list:
        f.write(inp_img_path+filename+"\n")
    f.close()


for dir in dir_list:
    one_dir(img_path+dir,txt_path+dir)