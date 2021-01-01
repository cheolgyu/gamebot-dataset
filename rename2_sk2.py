from datetime import datetime
import os

img_patrh =  "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_sk2/project_7"

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

def dir_5():
    # 창닫기
    inp_dir = img_patrh+"/5/"
    inp_data = "0.956291 0.050000 0.058007 0.088406\n6 0.903595 0.771014 0.181373 0.168116\n7 0.230801 0.547826 0.100490 0.168116\n"
    mk_file(inp_dir,inp_data)
def dir_1():
    inp_dir = img_patrh+"/1/"
    inp_data = "1 0.933415 0.906522 0.066176 0.140580\n26 0.488971 0.445783 0.235860 0.361446\n27 0.828337 0.906627 0.244910 0.122490\n"
    mk_file(inp_dir,inp_data)
    
def dir_2():
    # 기본모드-가방풀+
    inp_dir = img_patrh+"/2/"
    inp_data = "2 0.097631 0.057246 0.090686 0.097101\n25 0.797511 0.901104 0.079186 0.135542\n"
    mk_file(inp_dir,inp_data)
def dir_2_1():
    # 기본모드-가방풀
    # 추가: 스마트키on
    inp_dir = img_patrh+"/2_1/"
    inp_data = "2 0.097631 0.057246 0.090686 0.097101\n16 0.879229 0.790833 0.121241 0.208333\n24 0.036482 0.052711 0.054864 0.095382\n"
    mk_file(inp_dir,inp_data)
def dir_2_2():
    # 기본모드-가방풀
    # 추가: 스마트키-off
    inp_dir = img_patrh+"/2_2/"
    inp_data = "2 0.097631 0.057246 0.090686 0.097101\n15 0.879229 0.790833 0.121241 0.208333\n24 0.036482 0.052711 0.054864 0.095382\n"
    mk_file(inp_dir,inp_data)

def dir_3():
    # 가방기본화면-분해좌,홈
    inp_dir = img_patrh+"/3/"
    inp_data = "3 0.769608 0.775362 0.225490 0.136232\n0.956291 0.050000 0.058007 0.088406\n"
    mk_file(inp_dir,inp_data)

def dir_4():
    # 분해선택활성화-일반,고급,홈
    inp_dir = img_patrh+"/4/"
    inp_data = "0.956291 0.050000 0.058007 0.088406\n4 0.645016 0.675362 0.100490 0.081159\n5 0.743056 0.674638 0.097222 0.073913\n"
    mk_file(inp_dir,inp_data)

def dir_5_0_0():
    # 분해아이템선택화면-일반.on/off,고급.on/off,홈
    # 추가: 일반.on,고급.off
    inp_dir = img_patrh+"/5_0_0/"
    inp_data = "4 0.645016 0.675362 0.100490 0.081159\n0.956291 0.050000 0.058007 0.088406\n6 0.903595 0.771014 0.181373 0.168116\n7 0.230801 0.547826 0.100490 0.168116\n"
    mk_file(inp_dir,inp_data)
def dir_5_0_1():
    # 분해아이템선택화면-일반.on/off,고급.on/off,홈
    # 추가: 일반.off,고급.on
    inp_dir = img_patrh+"/5_0_1/"
    inp_data = "5 0.743056 0.674638 0.097222 0.073913\n0.956291 0.050000 0.058007 0.088406\n6 0.903595 0.771014 0.181373 0.168116\n7 0.230801 0.547826 0.100490 0.168116\n"
    mk_file(inp_dir,inp_data)    

def dir_5_1():
    # 분해아이템선택화면-,홈 일반.off,고급.off
    inp_dir = img_patrh+"/5_1/"
    inp_data = "0.956291 0.050000 0.058007 0.088406\n6 0.903595 0.771014 0.181373 0.168116\n7 0.184641 0.547101 0.086601 0.157971\n"
    mk_file(inp_dir,inp_data)    

def dir_6():
    # 분해팝업.확인
    # 추가: 홈
    inp_dir = img_patrh+"/6/"
    inp_data = "8 0.524101 0.500000 0.776961 0.515942\n9 0.613971 0.663043 0.247549 0.155072\n0 0.956291 0.050000 0.058007 0.088406\n"
    mk_file(inp_dir,inp_data)

def dir_7():
    # 창닫기
    inp_dir = img_patrh+"/7/"
    inp_data = "10 0.428922 0.479710 0.104575 0.171014\n11 0.498775 0.221014 0.178922 0.120290\n"
    mk_file(inp_dir,inp_data)
def dir_7_1():
    # 창닫기
    inp_dir = img_patrh+"/7_1/"
    inp_data = "10 0.361928 0.484783 0.104575 0.169565\n11 0.498775 0.221014 0.178922 0.120290\n"
    mk_file(inp_dir,inp_data)

def dir_8():
    #  12-0.스킵
    inp_dir = img_patrh+"/8/"
    inp_data = "12 0.928102 0.072500 0.119361 0.085000\n"
    mk_file(inp_dir,inp_data)

def dir_9():
    # 13-1 확인 14-2 취소 12 스킵
    inp_dir = img_patrh+"/9/"
    inp_data = "13 0.613715 0.699846 0.204861 0.121914\n14 0.387587 0.699074 0.203993 0.111111\n12 0.928102 0.072500 0.119361 0.085000\n "
    mk_file(inp_dir,inp_data)

def dir_10():
    #  15-3.스마.off
    inp_dir = img_patrh+"/10/"
    inp_data = "15 0.879229 0.790833 0.121241 0.208333\n24 0.036482 0.052711 0.054864 0.095382\n"
    mk_file(inp_dir,inp_data)
def dir_11():
    #  16-4.스마.on
    inp_dir = img_patrh+"/11/"
    inp_data = "16 0.879229 0.790833 0.121241 0.208333\n24 0.036482 0.052711 0.054864 0.095382\n"
    mk_file(inp_dir,inp_data)

def dir_12():
    #  12 팀편성
    inp_dir = img_patrh+"/12/"
    inp_data = "17 0.500000 0.498457 0.913194 0.651235\n18 0.486979 0.650463 0.477431 0.331790\n19 0.601562 0.715278 0.197917 0.158951\n"
    mk_file(inp_dir,inp_data)
def dir_13():
    #  13 미니팝업
    inp_dir = img_patrh+"/13/"
    inp_data = "20 0.293837 0.401235 0.556424 0.709877\n21 0.296441 0.109568 0.459201 0.120370\n22 0.492622 0.105710 0.070312 0.128086\n"
    mk_file(inp_dir,inp_data)

def dir_1_0():
    inp_dir = img_patrh+"/1_0/"
    inp_data = "1 0.933415 0.906522 0.066176 0.140580\n26 0.488971 0.445783 0.235860 0.361446\n27 0.828337 0.906627 0.244910 0.122490\n"
    mk_file(inp_dir,inp_data)
def dir_1_1_0():
    inp_dir = img_patrh+"/1_1_0/"
    inp_data = "0 0.933277 0.924174 0.077703 0.109610\n26 0.488971 0.445783 0.235860 0.361446\n28 0.828337 0.906627 0.244910 0.122490\n"
    mk_file(inp_dir,inp_data)
def dir_1_1_1():
    inp_dir = img_patrh+"/1_1_1/"
    inp_data = "26 0.488971 0.445783 0.235860 0.361446\n28 0.828337 0.906627 0.244910 0.122490\n"
    mk_file(inp_dir,inp_data)
def dir_14():
    inp_dir = img_patrh+"/14/"
    inp_data = "23 0.522059 0.492972 0.727376 0.638554\n24 0.036482 0.052711 0.054864 0.095382\n"
    mk_file(inp_dir,inp_data)
def dir_15():
    inp_dir = img_patrh+"/15/"
    inp_data = "0.956291 0.050000 0.058007 0.088406\n"
    mk_file(inp_dir,inp_data)

def dir_16():
    inp_dir = img_patrh+"/16/"
    inp_data = "\n"
    mk_file(inp_dir,inp_data)

def dir_17():
    inp_dir = img_patrh+"/17/"
    inp_data = "24 0.036482 0.052711 0.054864 0.095382\n"
    mk_file(inp_dir,inp_data)
def dir_18():
    inp_dir = img_patrh+"/18/"
    inp_data = "25 0.797511 0.901104 0.079186 0.135542\n"
    mk_file(inp_dir,inp_data)
def dir_19():
    inp_dir = img_patrh+"/19/"
    inp_data = "26 0.488971 0.445783 0.235860 0.361446\n27 0.828337 0.906627 0.244910 0.122490\n"
    mk_file(inp_dir,inp_data)
def dir_20():
    inp_dir = img_patrh+"/20/"
    inp_data = "24 0.036482 0.052711 0.054864 0.095382\n15 0.879229 0.790833 0.121241 0.208333\n"
    mk_file(inp_dir,inp_data)
def dir_21():
    inp_dir = img_patrh+"/21/"
    inp_data = "26 0.488971 0.445783 0.235860 0.361446\n28 0.828337 0.906627 0.244910 0.122490\n"
    mk_file(inp_dir,inp_data)


dir_17()   
dir_18()   
dir_19()   
dir_20()   
dir_21()   
dir_16()   
dir_15()   
dir_14()   
dir_13()   
dir_12()   
dir_11()   
dir_10()   
dir_9()    
dir_8()    
dir_7()    
dir_7_1()  
dir_6()    
dir_5_1()  
dir_5_0_1()
dir_5_0_0()
dir_4()    
dir_3()    
dir_2_2()  
dir_2_1()  
dir_2()    
dir_1()    
dir_1_0()
dir_1_1_0()
dir_1_1_1()
  
