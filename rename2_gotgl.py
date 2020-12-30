from datetime import datetime
import os

img_patrh_p1 =  "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_gotgl/p1"

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

class p1:
    def gotgl_001():
        inp_dir = img_patrh_p1+"/gotgl_001/"
        inp_data = "\
1 0.945136 0.788153 0.087104 0.128514\n\
4 0.112839 0.288655 0.053733 0.089357\n\
4 0.520645 0.479920 0.046946 0.074297\n\
5 0.496606 0.263554 0.047511 0.081325\n\
6 0.292986 0.192771 0.046380 0.090361\n\
7 0.333428 0.373494 0.052602 0.082329\n\
8 0.168269 0.559237 0.053733 0.096386\n\
"
        mk_file(inp_dir,inp_data)

    def gotgl_002():
        inp_dir = img_patrh_p1+"/gotgl_002/"
        inp_data = "\
0 0.949095 0.770582 0.075792 0.137550\n\
3 0.876131 0.783133 0.098416 0.122490\n\
4 0.112839 0.288655 0.053733 0.089357\n\
4 0.520645 0.479920 0.046946 0.074297\n\
5 0.496606 0.263554 0.047511 0.081325\n\
6 0.292986 0.192771 0.046380 0.090361\n\
7 0.333428 0.373494 0.052602 0.082329\n\
8 0.168269 0.559237 0.053733 0.096386\n\
"
        mk_file(inp_dir,inp_data)        
    def gotgl_003():
        inp_dir = img_patrh_p1+"/gotgl_003/"
        inp_data = "\
0 0.949095 0.770582 0.075792 0.137550\n\
3 0.876131 0.783133 0.098416 0.122490\n\
"
        mk_file(inp_dir,inp_data) 

    def gotgl_004():
        inp_dir = img_patrh_p1+"/gotgl_004/"
        inp_data = "\
1 0.945136 0.788153 0.087104 0.128514\n\
3 0.876131 0.783133 0.098416 0.122490\n\
"
        mk_file(inp_dir,inp_data)                     
    
    def gotgl_005():
        inp_dir = img_patrh_p1+"/gotgl_005/"
        inp_data = "\
1 0.945136 0.788153 0.087104 0.128514\n\
3 0.876131 0.783133 0.098416 0.122490\n\
"
        mk_file(inp_dir,inp_data)       
    # 6 카메라 복잡 건너뜀
    
    def gotgl_007():
        inp_dir = img_patrh_p1+"/gotgl_007/"
        inp_data = "\
0 0.948529 0.790161 0.065611 0.130522\n\
2 0.499434 0.801205 0.225113 0.132530\n\
4 0.104921 0.248494 0.045814 0.087349\n\
4 0.172511 0.546687 0.045249 0.085341\n\
4 0.286765 0.338855 0.042986 0.081325\n\
4 0.745475 0.554217 0.042986 0.074297\n\
"
        mk_file(inp_dir,inp_data)                     

# 8 카메라 복잡 건너뜀

# 9부턴 객체아닌것 인식용 + 창닫기
    def gotgl_009():
        ll = list(range(9,16))

        for v in ll :
            inp_dir = img_patrh_p1+"/gotgl_00"+str(v)+"/"
            inp_data = "\
9 0.967760 0.046185 0.046380 0.072289\n\
    "
            mk_file(inp_dir,inp_data)   


p1.gotgl_001()     
p1.gotgl_002()     
p1.gotgl_003()     
p1.gotgl_004()     
p1.gotgl_005()     
p1.gotgl_007()     
p1.gotgl_009()        
