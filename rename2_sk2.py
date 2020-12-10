from datetime import datetime
import os

img_patrh =  "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_sk2/project_1"
img_patrh_p2 =  "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_sk2/project_2"
img_patrh_p3 =  "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_sk2/project_3"

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

def p2_skip():
    #  12-0.스킵
    inp_dir = img_patrh_p2+"/8/"
    inp_data = "0 0.928102 0.072500 0.119361 0.085000\n"
    mk_file(inp_dir,inp_data)

def p2_skip_popup():
    # 13-1 확인 14-2 취소 12 스킵
    inp_dir = img_patrh_p2+"/9/"
    inp_data = "1 0.613715 0.699846 0.204861 0.121914\n2 0.387587 0.699074 0.203993 0.111111\n0 0.928102 0.072500 0.119361 0.085000\n "
    mk_file(inp_dir,inp_data)

def p2_smartkey_off():
    #  15-3.스마.off
    inp_dir = img_patrh_p2+"/10/"
    inp_data = "3 0.879229 0.790833 0.121241 0.208333\n"
    mk_file(inp_dir,inp_data)
def p2_smartkey_on():
    #  16-4.스마.off
    inp_dir = img_patrh_p2+"/11/"
    inp_data = "4 0.879229 0.790833 0.121241 0.208333\n"
    mk_file(inp_dir,inp_data)

##################################################################
#                   p3 
##################################################################
def p3_dir_1():
    inp_dir = img_patrh_p3+"/1/"
    inp_data = "1 0.933415 0.906522 0.066176 0.140580\n"
    mk_file(inp_dir,inp_data)
      
def p3_dir_2():
    # 기본모드-가방풀+
    inp_dir = img_patrh_p3+"/2/"
    inp_data = "2 0.097631 0.057246 0.090686 0.097101\n"
    mk_file(inp_dir,inp_data)
def p3_dir_2_1():
    # 기본모드-가방풀
    # 추가: 스마트키on
    inp_dir = img_patrh_p3+"/2_1/"
    inp_data = "2 0.097631 0.057246 0.090686 0.097101\n16 0.879229 0.790833 0.121241 0.208333\n"
    mk_file(inp_dir,inp_data)
def p3_dir_2_2():
    # 기본모드-가방풀
    # 추가: 스마트키-off
    inp_dir = img_patrh_p3+"/2_2/"
    inp_data = "2 0.097631 0.057246 0.090686 0.097101\n15 0.879229 0.790833 0.121241 0.208333\n"
    mk_file(inp_dir,inp_data)

def p3_dir_3():
    # 가방기본화면-분해좌,홈
    inp_dir = img_patrh_p3+"/3/"
    inp_data = "3 0.769608 0.775362 0.225490 0.136232\n0.956291 0.050000 0.058007 0.088406\n"
    mk_file(inp_dir,inp_data)

def p3_dir_4():
    # 분해선택활성화-일반,고급,홈
    inp_dir = img_patrh_p3+"/4/"
    inp_data = "0.956291 0.050000 0.058007 0.088406\n4 0.645016 0.675362 0.100490 0.081159\n5 0.743056 0.674638 0.097222 0.073913\n"
    mk_file(inp_dir,inp_data)

def p3_dir_5_0_0():
    # 분해아이템선택화면-일반.on/off,고급.on/off,홈
    # 추가: 일반.on,고급.off
    inp_dir = img_patrh_p3+"/5_0_0/"
    inp_data = "4 0.645016 0.675362 0.100490 0.081159\n0.956291 0.050000 0.058007 0.088406\n6 0.903595 0.771014 0.181373 0.168116\n7 0.230801 0.547826 0.100490 0.168116\n"
    mk_file(inp_dir,inp_data)
def p3_dir_5_0_1():
    # 분해아이템선택화면-일반.on/off,고급.on/off,홈
    # 추가: 일반.off,고급.on
    inp_dir = img_patrh_p3+"/5_0_1/"
    inp_data = "5 0.743056 0.674638 0.097222 0.073913\n0.956291 0.050000 0.058007 0.088406\n6 0.903595 0.771014 0.181373 0.168116\n7 0.230801 0.547826 0.100490 0.168116\n"
    mk_file(inp_dir,inp_data)    

def p3_dir_5_1():
    # 분해아이템선택화면-,홈 일반.off,고급.off
    inp_dir = img_patrh_p3+"/5_1/"
    inp_data = "0.956291 0.050000 0.058007 0.088406\n6 0.903595 0.771014 0.181373 0.168116\n7 0.184641 0.547101 0.086601 0.157971\n"
    mk_file(inp_dir,inp_data)    

def p3_dir_6():
    # 분해팝업.확인
    # 추가: 홈
    inp_dir = img_patrh_p3+"/6/"
    inp_data = "8 0.524101 0.500000 0.776961 0.515942\n9 0.613971 0.663043 0.247549 0.155072\n0 0.956291 0.050000 0.058007 0.088406\n"
    mk_file(inp_dir,inp_data)

def p3_dir_7():
    # 창닫기
    inp_dir = img_patrh_p3+"/7/"
    inp_data = "10 0.428922 0.479710 0.104575 0.171014\n11 0.498775 0.221014 0.178922 0.120290\n"
    mk_file(inp_dir,inp_data)
def p3_dir_7_1():
    # 창닫기
    inp_dir = img_patrh_p3+"/7_1/"
    inp_data = "10 0.361928 0.484783 0.104575 0.169565\n11 0.498775 0.221014 0.178922 0.120290\n"
    mk_file(inp_dir,inp_data)

def p3_skip():
    #  12-0.스킵
    inp_dir = img_patrh_p3+"/8/"
    inp_data = "12 0.928102 0.072500 0.119361 0.085000\n"
    mk_file(inp_dir,inp_data)

def p3_skip_popup():
    # 13-1 확인 14-2 취소 12 스킵
    inp_dir = img_patrh_p3+"/9/"
    inp_data = "13 0.613715 0.699846 0.204861 0.121914\n14 0.387587 0.699074 0.203993 0.111111\n12 0.928102 0.072500 0.119361 0.085000\n "
    mk_file(inp_dir,inp_data)

def p3_smartkey_off():
    #  15-3.스마.off
    inp_dir = img_patrh_p3+"/10/"
    inp_data = "15 0.879229 0.790833 0.121241 0.208333\n"
    mk_file(inp_dir,inp_data)
def p3_smartkey_on():
    #  16-4.스마.on
    inp_dir = img_patrh_p3+"/11/"
    inp_data = "16 0.879229 0.790833 0.121241 0.208333\n"
    mk_file(inp_dir,inp_data)



p3_dir_1()
p3_dir_2()
p3_dir_2_1()
p3_dir_2_2()
p3_dir_3()
p3_dir_4()
p3_dir_5_0_0()
p3_dir_5_0_1()
p3_dir_5_1()
p3_dir_6()
p3_dir_7()
p3_dir_7_1()
p3_skip()
p3_skip_popup()
p3_smartkey_off()
p3_smartkey_on()