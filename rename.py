import os
from os.path import getsize
import random
import math
from datetime import datetime
import random
import shutil
import copy

def filename():
    (dt, micro) = datetime.utcnow().strftime('%Y%m%d%H%M%S.%f').split('.')
    dt = "%s%03d" % (dt, int(micro) / 1000)
    r=random.randrange(1,999)
    return str(r)+dt

current_milli_time = lambda: int(round(time.time() * 1000))
ratio=0.1



project="baram_3"
path = "./"+project+"/img/all/"
file_list = os.listdir(path)

train_str="ds/"+project+"/img/"
valid_str="ds/"+project+"/img/"
train_txt="./"+project+"/train.txt"
valid_txt="./"+project+"/valid.txt"

#print ("file_list: {}".format(file_list))
classes=79
cat_list=[]

for i in range(classes):
    cat_list.append([])

at_list=[]
#print ("cat_list size:"+str(len(cat_list)))
all_cnt=0
# 복사본 리네임
def aa():
    for file in file_list:
        if file.endswith(".jpg") and  file.find("복사본") != -1 :
            print ("size::"+str(getsize(path+file)))
            print ("f::"+str(path+file))
            file_name=file.split(".")
            new_filename=str(filename())+".jpg"

            os.rename(path+file,path+new_filename)

#jpg=> .jpg
def bb():
    for file in file_list:
        if file.endswith("jpg") and  file.find(".") == -1 :
            print ("f::"+str(path+file))
            file_name=file.split("jpg")
            new_filename=file_name[0]+".jpg"

            os.rename(path+file,path+new_filename)

# n번클랫스 텍스트파일 초기화
def cc():
    for file in file_list:
        if file.endswith("txt") and  getsize(path+file) > 0 :
           
            f = open(path+file, 'r')
            line = f.readline()
            d = line.split(" ")
            class_id = d[0]
            f.close()
            if(class_id=="4"):
                os.remove(path+file)
            
#bb()
#cc()

# 라벨4번이 인식이 잘안됨. 4번만 뽑아서 작게 훈련후 되나 태스트해보기.
def dd():
    str="['test_00001184.jpg', '13920200813085523191.jpg', 'test_00001022.jpg', 'test_00001015.jpg', 'test_00001016.jpg', 'test_00001188.jpg', 't4_00000205.jpg', 'test_00001199.jpg', 'test_00001018.jpg', 't4_00000113.jpg', 'test_00001186.jpg', 'test_00001021.jpg', 'test_00001202.jpg', 'test_00000872.jpg', 'test_00001187.jpg', 'test_00001194.jpg', 'test_00001027.jpg', 'test_00001028.jpg', 'test_00001205.jpg', 'test_00001179.jpg', 't2_00000230.jpg', 'test_00001037.jpg', 'test_00001032.jpg', 'test_00001012.jpg', 'test_00001197.jpg', 'test_00001013.jpg', 'test_00000875.jpg', 't2_00000277.jpg', 'test_00001190.jpg', 'test_00001017.jpg', 'test_00000868.jpg', 'test_00001183.jpg', 't6_00001990.jpg', 't4_00000115.jpg', 'test_00001195.jpg', 'test_00001200.jpg', 'test_00001172.jpg', 'test_00001174.jpg', 'test_00001173.jpg', 'test_00000873.jpg', 'test_00000874.jpg', 'test_00000871.jpg', 'test_00001031.jpg', 'test_00001192.jpg', 'test_00001019.jpg', 'test_00001024.jpg', 'test_00001203.jpg', 'test_00000870.jpg', 'test_00001177.jpg', 'test_00001206.jpg', 'test_00001026.jpg', 'test_00001181.jpg', 'test_00001193.jpg', 'test_00001191.jpg', 'test_00000869.jpg', 'test_00001196.jpg', 'test_00001033.jpg', 'test_00001035.jpg', 't3_00000316.jpg', '15220200813085523188.jpg', 'test_00001180.jpg', 'test_00001038.jpg', 'test_00001182.jpg', 'test_00001201.jpg', 'test_00001039.jpg', 'test_00001034.jpg', 'test_00001198.jpg', 'test_00001023.jpg', 'test_00001030.jpg', 'test_00001176.jpg', 'test_00001029.jpg', 'test_00001204.jpg', '10120200813085523254.jpg', 'test_00001189.jpg', 'test_00001178.jpg', 'test_00001036.jpg', '17920200813085523078.jpg', 'test_00001025.jpg', 't3_00000322.jpg', 'test_00001014.jpg', 'test_00001185.jpg', 'test_00001020.jpg', 'test_00001175.jpg','t6_00002404.jpg', 't3_00000318.jpg', 't3_00000372.jpg', 't6_00000390.jpg', 't3_00000464.jpg', 't3_00000320.jpg','t6_00002411.jpg', 't6_00002597.jpg', 't6_00002318.jpg', 't6_00002371.jpg','t6_00002240.jpg','t6_00000825.jpg', 't4_00000231.jpg', 't4_00000043.jpg', 'test_00001104.jpg', 't4_00000047.jpg', 'test_00001103.jpg', 't4_00000039.jpg', 't4_00000032.jpg', 'test_00001105.jpg', 'test_00001106.jpg', 't4_00000036.jpg', 'test_00001108.jpg', 't4_00000037.jpg', 't4_00000040.jpg', 't4_00000034.jpg', 't4_00000045.jpg', 't4_00000046.jpg', 't4_00000173.jpg', 't6_00000765.jpg', 't4_00000042.jpg', 'test_00001107.jpg', 't4_00000044.jpg', 't6_00000976.jpg', 't4_00000035.jpg', 't4_00000041.jpg', 't4_00000048.jpg', 't4_00000033.jpg', 't4_00000038.jpg','test_00000857.jpg', 'test_00000434.jpg', 'test_00000424.jpg', 'test_00000425.jpg', 'test_00001158.jpg', 'test_00000436.jpg', 'test_00000437.jpg', 'test_00001160.jpg', 'test_00000606.jpg', '17020200813085523176.jpg', 'test_00000801.jpg', 'test_00000794.jpg', 'test_00000446.jpg', 'test_00000449.jpg', 'test_00000444.jpg', 'test_00001146.jpg', 'test_00000441.jpg', 'test_00000803.jpg', 'test_00000799.jpg', 't3_00000298.jpg', 'test_00000859.jpg', 'test_00001147.jpg', 'test_00000602.jpg', 't6_00000953.jpg', 'test_00001150.jpg', 'test_00000607.jpg', 'test_00000858.jpg', 't3_00000303.jpg', 'test_00001154.jpg', 'test_00000450.jpg', 'test_00000609.jpg', '13520200813085523174.jpg', '67920200813085523232.jpg', 'test_00000796.jpg', 'test_00000439.jpg', 'test_00000797.jpg', 'test_00000597.jpg', 'test_00000445.jpg', 'test_00000608.jpg', 't3_00000294.jpg', '14620200813085523173.jpg', 'test_00001149.jpg', 'test_00000443.jpg', 'test_00000423.jpg', 'test_00001162.jpg', 'test_00000452.jpg', 'test_00000611.jpg', 'test_00000605.jpg', 'test_00000440.jpg', 'test_00001148.jpg', 'test_00000451.jpg', 't6_00000952.jpg', 'test_00001156.jpg', 'test_00000435.jpg', 'test_00000802.jpg', 't3_00000301.jpg', 'test_00000798.jpg', 'test_00000438.jpg', 'test_00001145.jpg', 'test_00001157.jpg', 'test_00001155.jpg', 'test_00000421.jpg', 'test_00001152.jpg', 't4_00000294.jpg', 'test_00001151.jpg', 'test_00000795.jpg', 'test_00000603.jpg', 't4_00000106.jpg', 'test_00000422.jpg', 't6_00002256.jpg', 'test_00000601.jpg', 'test_00001161.jpg', 't4_00000107.jpg', 'test_00000442.jpg', 't2_00000115.jpg', 't3_00000296.jpg', 'test_00001153.jpg', 'test_00000800.jpg', 'test_00000793.jpg', 'test_00000447.jpg', 'test_00000610.jpg', 'test_00000448.jpg', 'test_00001159.jpg', 'test_00000604.jpg', 'test_00000860.jpg','t6_00000542.jpg', 't6_00000520.jpg', 't6_00000533.jpg', 't6_00000535.jpg', 't6_00000525.jpg', 't6_00000522.jpg', 't6_00000544.jpg', 't6_00000545.jpg', 't6_00000526.jpg', 't6_00000536.jpg', 't6_00000532.jpg', 't6_00000521.jpg', 't6_00000534.jpg', 't6_00000529.jpg', 't6_00000527.jpg', 't6_00000538.jpg', 't6_00000530.jpg', 't6_00000519.jpg', 't6_00000523.jpg', 't6_00000518.jpg', 't6_00000543.jpg', 't6_00000524.jpg', 't6_00000537.jpg', 't6_00000236.jpg', 't6_00000539.jpg', 't6_00000528.jpg', 't6_00000540.jpg', 't6_00000541.jpg', 't6_00000531.jpg','t6_00000373.jpg', 't6_00000566.jpg', 't6_00000320.jpg', 't6_00002278.jpg', 't6_00000563.jpg', 't6_00000588.jpg', 't6_00000375.jpg','baram_test1_class_2_9.jpg']"

    str=str.replace("'","")
    str=str.replace("[","")
    str=str.replace("]","")
    str=str.replace(" ","")
    arr=str.split(",")
    for i in arr :
        print(i)
        new_dir= path+"new_4123/"   
        if not  os.path.isdir(new_dir)  :
            os.makedirs(new_dir)
        shutil.copy(path+i, new_dir+i)
        arr = i.split(".jpg")
        txt = arr[0]+".txt"
        shutil.copy(path+txt, new_dir+txt)
    
#dd()           
# 리네임 폴더내 파일
def ee():
    for file in file_list:
        if file.endswith(".jpg") :
            print ("f::"+str(path+file))
            new_f_str=str("baram_27_"+filename())

            arr_name=file.split(".")
            ori_txt=arr_name[0]+".txt"
            ori_jpg=arr_name[0]+".jpg"
            
            new_file_jpg=new_f_str+".jpg"
            new_file_txt=new_f_str+".txt"

            os.rename(path+ori_jpg,path+new_file_jpg)
            os.rename(path+ori_txt,path+new_file_txt)

# 클래스별 폴더만들고 파일 복사
def ff():
    arr = []
    for i in range(80):
        arr.append([])

    for file in file_list:
        if file.endswith("txt") and  getsize(path+file) > 0 :
            f = open(path+file, 'r')
            line = f.readline()
            d = line.split(" ")
            class_id = d[0]
            f.close()
            arr[int(class_id)].append(file)

    for i , v  in enumerate(arr):
        cnt=len(v)
        if cnt>0 :
            print("class="+str(i)+" cnt="+str(cnt))
            for j , str_txt  in enumerate(v): 
                str_newname="class_"+str(i)+"_"+filename()
                dir= path+"class_"+str(i)+"/"  
                if not  os.path.isdir(dir)  :
                    os.makedirs(dir) 

                str_jpg=copy.deepcopy(str_txt)
                str_jpg=str_jpg.replace(".txt",".jpg")
                print(str_txt+"     "+str_jpg)
                shutil.move(path+str_txt, dir+str_newname+".txt")
                shutil.move(path+str_jpg, dir+str_newname+".jpg")
# ff()
# 클래스별 폴더만들고 오래된 폴더에서 현재폴더로 복사
def gg():
    project_old="baram"
    path_old = "./"+project_old+"/img/new/"
    file_list_old = os.listdir(path_old)

    arr = []
    for i in range(80):
        arr.append([])

    for file in file_list_old:
        if file.endswith("txt") and  getsize(path_old+file) > 0 :
            print(path_old+file)
            print(str(getsize(path_old+file)))
            f = open(path_old+file, 'r+')
            line = f.readline()
            d = line.split(" ")
            class_id = d[0]
            f.close()
            arr[int(class_id)].append(file)

    for i , v  in enumerate(arr):
        cnt=len(v)
        if cnt>0 :dd()

# 폴더내 class_id 재정의
def hh(id_new, id_old):
    project="baram_3"
    path = "./"+project+"/img/class_"+str(id_old)+"/"
    path_new = "./"+project+"/img_new/class_"+str(id_new)+"/"
    file_list = os.listdir(path)

    arr = []
    for i in range(80):
        arr.append([])

    for file in file_list:
        if file.endswith("txt") and  getsize(path+file) > 0 :
            str_jpg=copy.deepcopy(file)
            str_jpg=str_jpg.replace(".txt",".jpg")
            fnm="class_"+str(id_new)+"_"+filename()
            f = open(path+file, 'r+')
            line = f.readline()
            d = line.split(" ")
            class_id = d[0]
            f.close()
            new_line=str(id_new)+" "+d[1]+" "+d[2]+" "+d[3]+" "+d[4]

            if not  os.path.isdir(path_new)  :
                os.makedirs(path_new)
            

            shutil.copy(path+str_jpg, path_new+fnm+".jpg")

            f = open(path_new+fnm+".txt", 'w', encoding="UTF8")
            f.write(new_line+"\n")
            f.close()

#gg()
#hh(7,6)
#hh(6,4)