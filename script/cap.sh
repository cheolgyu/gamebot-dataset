

# chmod +x ./cap.sh
#echo "첫 번째 파라미터: $1"
#echo "cap.sh $1"
#echo "../ds/ds_sk2/img/sk2_00$1" 
#echo "/home/cheolgyu/다운로드/sk2_00$1.mp4"
mkdir "../ds/ds_sk2/img/sk2_00$1" 
../yolo_mark "../ds/ds_sk2/img/sk2_00$1" cap_video "/home/cheolgyu/다운로드/sk2_00$1.mp4" 10

