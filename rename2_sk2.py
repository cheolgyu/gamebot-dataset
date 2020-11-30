from datetime import datetime
import os

img_patrh =  "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_sk2/project_1"
def mk_file(inp_dir,inp_data):
    file_list = os.listdir(inp_dir)
    for file in file_list:
        if file.endswith(".jpg")  :
            arr = file.split(".")
            file_txt = inp_dir+arr[0]+".txt"
            if os.path.exists(file_txt):
                os.remove(file_txt)
            f = open(file_txt, 'w')
            data = inp_data
            f.write(data)
            f.close()    
def screen_1():
    # 창닫기
    inp_dir = img_patrh+"/1/"
    inp_data = "1 0.933415 0.906522 0.066176 0.140580\n"
    mk_file(inp_dir,inp_data)
      
def screen_2():
    # 창닫기
    inp_dir = img_patrh+"/2/"
    inp_data = "2 0.097631 0.057246 0.090686 0.097101\n"
    mk_file(inp_dir,inp_data)
    
def screen_3():
    # 창닫기
    inp_dir = img_patrh+"/3/"
    inp_data = "3 0.769608 0.775362 0.225490 0.136232\n0.956291 0.050000 0.058007 0.088406\n"
    mk_file(inp_dir,inp_data)

def screen_4():
    # 창닫기
    inp_dir = img_patrh+"/4/"
    inp_data = "0.956291 0.050000 0.058007 0.088406\n4 0.645016 0.675362 0.100490 0.081159\n5 0.743056 0.674638 0.097222 0.073913\n"
    mk_file(inp_dir,inp_data)

def screen_5():
    # 창닫기
    inp_dir = img_patrh+"/5/"
    inp_data = "0.956291 0.050000 0.058007 0.088406\n6 0.903595 0.771014 0.181373 0.168116\n7 0.230801 0.547826 0.100490 0.168116\n"
    mk_file(inp_dir,inp_data)

def screen_5_1():
    # 창닫기
    inp_dir = img_patrh+"/5_1/"
    inp_data = "0.956291 0.050000 0.058007 0.088406\n6 0.903595 0.771014 0.181373 0.168116\n7 0.184641 0.547101 0.086601 0.157971\n"
    mk_file(inp_dir,inp_data)    

def screen_6():
    # 창닫기
    inp_dir = img_patrh+"/6/"
    inp_data = "8 0.524101 0.500000 0.776961 0.515942\n9 0.613971 0.663043 0.247549 0.155072\n"
    mk_file(inp_dir,inp_data)

def screen_7():
    # 창닫기
    inp_dir = img_patrh+"/7/"
    inp_data = "10 0.428922 0.479710 0.104575 0.171014\n11 0.498775 0.221014 0.178922 0.120290\n"
    mk_file(inp_dir,inp_data)
def screen_7_1():
    # 창닫기
    inp_dir = img_patrh+"/7_1/"
    inp_data = "10 0.361928 0.484783 0.104575 0.169565\n11 0.498775 0.221014 0.178922 0.120290\n"
    mk_file(inp_dir,inp_data)

screen_1()
screen_2()
screen_3()
screen_4()
screen_5()
screen_5_1()
screen_6()
screen_7()
screen_7_1()
