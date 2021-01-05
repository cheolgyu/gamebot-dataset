

# chmod +x ./cap.sh
#echo "첫 번째 파라미터: $1"
#echo "cap.sh $1"
#echo "../ds/ds_baram/img/baram_00$1" 
#echo "/home/cheolgyu/다운로드/baram_00$1.mp4"
mkdir -p "../ds/ds_baram/img/baram_00$1" 
../yolo_mark "../ds/ds_baram/img/baram_00$1" cap_video "/home/cheolgyu/다운로드/baram_00$1.mp4" 10

