from datetime import datetime
import os


obj=["0 0.812500 0.157639 0.371875 0.123611","1 0.572656 0.868056 0.150000 0.097222","2 0.757812 0.918750 0.195312 0.126389","3 0.921484 0.890972 0.133594 0.104167","4 0.919922 0.048611 0.160156 0.097222","5 0.498828 0.651389 0.136719 0.091667","6 0.416016 0.863194 0.163281 0.101389","7 0.423828 0.741667 0.136719 0.111111"]
arr_path = ["/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_fivestars/0_쾌시작","/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_fivestars/1_쾌정보-확인","/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_fivestars/2_전투시작","/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_fivestars/3_월드맵","/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_fivestars/4_건너뛰기","/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_fivestars/5_쾌스트보상-확인","/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_fivestars/6_렙업확인","/home/cheolgyu/workspace/gamebot/gamebot-dataset/ds/ds_fivestars/7_컨텐츠오픈확인"]


def set():
    for index in range(len(arr_path)):
        path = arr_path[index]+"/"
        file_list = os.listdir(path+"/")
        for file in file_list:
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