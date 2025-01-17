from datetime import datetime
import os

img_patrh =  "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_baram/p1"

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

dir_name = "/baram_00"
def dir_1_4():
    
    for i in  range(1, 5):
        inp_dir = img_patrh+dir_name+"%s/" %i
        inp_data = "0 0.067029 0.358521 0.077899 0.096463\n6 0.951801 0.582075 0.062500 0.115094\n"
        mk_file(inp_dir,inp_data)
def dir_5_6():
    
    for i in  range(5, 7):
        inp_dir = img_patrh+dir_name+"%s/" %i
        inp_data = "0 0.067029 0.358521 0.077899 0.096463\n5 0.951801 0.582075 0.062500 0.115094\n"
        mk_file(inp_dir,inp_data)


def dir_7():
    inp_dir = img_patrh+dir_name+"7/"
    inp_data = "1 0.962394 0.050000 0.056144 0.084906\n4 0.915254 0.555660 0.097458 0.107547\n4 0.915254 0.833962 0.097458 0.098113\n"
    mk_file(inp_dir,inp_data)
def dir_8():
    inp_dir = img_patrh+dir_name+"8/"
    inp_data = "1 0.962394 0.050000 0.056144 0.084906\n3 0.817797 0.412264 0.101695 0.118868\n4 0.916314 0.687736 0.103814 0.115094\n"
    mk_file(inp_dir,inp_data)    
def dir_9():
    inp_dir = img_patrh+dir_name+"9/"
    inp_data = "1 0.962394 0.050000 0.056144 0.084906\n3 0.817797 0.412264 0.101695 0.118868\n4 0.916314 0.687736 0.103814 0.115094\n"
    mk_file(inp_dir,inp_data)    
def dir_10():
    inp_dir = img_patrh+dir_name+"10/"
    inp_data = "2 0.435911 0.554717 0.126059 0.098113\n"
    mk_file(inp_dir,inp_data)  
def dir_11():
    inp_dir = img_patrh+dir_name+"11/"
    inp_data = "2 0.435911 0.554717 0.126059 0.098113\n"
    mk_file(inp_dir,inp_data)      
def dir_16_17():
    for i in  range(16, 18):
        inp_dir = img_patrh+dir_name+"%s/" %i
        inp_data = "6 0.951801 0.582075 0.062500 0.115094\n"
        mk_file(inp_dir,inp_data)    
def dir_18():
    inp_dir = img_patrh+dir_name+"18/"
    inp_data = "7 0.502551 0.498188 0.392857 0.423913\n8 0.501020 0.619565 0.134694 0.108696\n"
    mk_file(inp_dir,inp_data)   
def dir_19():
    inp_dir = img_patrh+dir_name+"19/"
    inp_data = "5 0.951801 0.582075 0.062500 0.115094\n"
    mk_file(inp_dir,inp_data)   
def dir_20():
    inp_dir = img_patrh+dir_name+"20/"
    inp_data = "5 0.951801 0.582075 0.062500 0.115094\n"
    mk_file(inp_dir,inp_data)   
def dir_21():
    inp_dir = img_patrh+dir_name+"21/"
    inp_data = "5 0.951801 0.582075 0.062500 0.115094\n"
    mk_file(inp_dir,inp_data)       
def dir_22():
    inp_dir = img_patrh+dir_name+"22/"
    inp_data = "0 0.067029 0.358521 0.077899 0.096463\n5 0.951801 0.582075 0.062500 0.115094\n"
    mk_file(inp_dir,inp_data)             
dir_1_4()
dir_5_6()
dir_7()
dir_8()
dir_9()
dir_10()
dir_11()
dir_16_17()
dir_18()
dir_19()
dir_20()
dir_21()
dir_22()    
