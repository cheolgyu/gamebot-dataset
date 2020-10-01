from datetime import datetime
import os

print("11111111111")
obj=[
    #"0 0.852734 0.275000 0.266406 0.150000", 일일히 손으로 
"1 0.882422 0.658333 0.202344 0.350000",
"2 0.827344 0.513194 0.321875 0.543056",
"3 0.681250 0.192361 0.323438 0.368056",
"4 0.940234 0.095139 0.111719 0.162500",
"5 0.736328 0.256250 0.299219 0.473611",
"6 0.516016 0.459722 0.566406 0.530556"]
arr_path = [
    #"/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_illusionc/o_쾌시작", 
    "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_illusionc/o_도전",
    "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_illusionc/o_알림",
    "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_illusionc/o_승리",
    "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_illusionc/o_스킵",
    "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_illusionc/o_패배",
    "/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_illusionc/o_보상획득"
    ]
print("2222222")

def set():
    for index in range(len(arr_path)):
        
        path = arr_path[index]+"/"
        file_list = os.listdir(path+"/")
        for file in file_list:
            print(file)
            if file.endswith(".jpg") :
                arr = file.split(".")
                file_txt = path+arr[0]+".txt"
                if os.path.exists(file_txt):
                    os.remove(file_txt)
                
                f = open(file_txt, 'w')
                data = obj[index]+"\n"
                f.write(data)
                f.close()

set()