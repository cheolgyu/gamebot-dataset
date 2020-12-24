# gamebot-dataset

녹화한것 스샷 만들기 ==> script/capture.sh, 이미지폴더 : ds_sk2/img   
스샷 폴더분류하기 ds_sk2/img ==> ds_sk2/project_n/1..999   
분류한 폴더에 어노테이션파일 생성하기 ==> rename2_sk2.py   
yoloy train.txt, valild.txt 만들기 ==> yolo/label_after2.py


## sk2(세븐나이츠2) 
```
분류한 폴더 정보


p5
        16. 비슷한객체들+ 홈.x 
        15. 비슷한객체들+ 홈.o
        14. 죽음
p4
        13. 미니팝업
        12. 팀편성
p3
        11. 스마트키on
        10. 스마트키off
        9. 스킵팝업
        8. 스킵화면
        7. 분해결과-2개
        7-1. 분해결과-3개
        6. 분해팝업
        5_1. 분해아이템선택 일반.off, 고급off,홈
        5_0_1. 분해아이템선택화면-일반.on/off,고급.on/off,홈
        5_0_0. 분해아이템선택화면-일반.on/off,고급.on/off,홈
        4. 분해선택활성화-일반,고급,홈
        3. 가방기본화면-분해좌,홈
        2_1. 기본모드-가방풀,스마트키on
        2. 기본모드-가방풀
        1. 절전화면.방치형o.가방가득.o
p5
        1_1_0. 절전화면.방치형x.가방가득o
        1_1_1. 절전화면.방치형x.가방가득x
        1_0. 절전화면.방치형o.가방가득.x
p2        
```
```
인식객체 좌표정보
0 0.956291 0.050000 0.058007 0.088406   --홈
1 0.933415 0.906522 0.066176 0.140580   --절전풀.방치o
2 0.097631 0.057246 0.090686 0.097101   --전체풀
3 0.769608 0.775362 0.225490 0.136232   --분해좌
4 0.645016 0.675362 0.100490 0.081159   --일반
5 0.743056 0.674638 0.097222 0.073913   --고급
6 0.903595 0.771014 0.181373 0.168116   --분해우
7 0.230801 0.547826 0.100490 0.168116   --금화위치.분해결과2.분해선택
7 0.184641 0.547101 0.086601 0.157971   --금화위치.분해결과3.분해선택

8 0.524101 0.500000 0.776961 0.515942   --분해팝업창
9 0.613971 0.663043 0.247549 0.155072   --분해팝업창.확인
10 0.428922 0.479710 0.104575 0.171014  --금화위치.분해결과2
10 0.361928 0.484783 0.104575 0.169565  --금화위치.분해결과3
11 0.498775 0.221014 0.178922 0.120290  --분해결과.텍스트
12 0.928102 0.072500 0.119361 0.085000  --스킵
13 0.613715 0.699846 0.204861 0.121914  --스킵확인
14 0.387587 0.699074 0.203993 0.111111  --스킵취소
15 0.879229 0.790833 0.121241 0.208333  --스마.off
16 0.879229 0.790833 0.121241 0.208333  --스마.on
17 0.500000 0.498457 0.913194 0.651235  --팀교체.전체
18 0.486979 0.650463 0.477431 0.331790  --팀교체.중간
19 0.601562 0.715278 0.197917 0.158951  --팀교체.진행
20 0.293837 0.401235 0.556424 0.709877  --도움.전체
21 0.296441 0.109568 0.459201 0.120370  --도움.중간
22 0.492622 0.105710 0.070312 0.128086  --도움.닫기
23 0.522059 0.492972 0.727376 0.638554  --전투패배팝업
0 0.933277 0.924174 0.077703 0.109610  --절전풀.방치x

```
fivestars

0. 쾌시작
1. 쾌정보-확인
2. 전투시작
3. 월드맵
4. 건너뛰기
5. 쾌스트보상-확인
6. 렙업확인
7. 컨텐츠오픈 확인

```







```
왕좌의게임

        0. 수령 
        1. 수령x5
        2. 수령확인
        3. 도움
        4. 할리스
        5. 식량
        6. 목재
        7. 석재
        8. 철광
        9. 음식
        10. 창닫기
```


1	우측-쾌완료-아이콘
2	우측-쾌받기-텍스트
3	자동텍스트
4	우측쾌비활성-반짝임 -삭제
5	우측쾌비활성
6	우측쾌활성
7	
8	
9	
10	알림-쾌스트수락창-타이틀
11	알림-쾌스트수락창-확인
12	전체화면-쾌스트완료-텍스트
13	전체화면-쾌스트건너뛰기
14	
15	
16	
17	
18	
19	
20	튜토리얼-시작텍스트
21	튜토리얼-시작버튼
22	튜토리얼-건너뛰기
23	튜토리얼-완료텍스트
24	
25	
26	
27	
28	
29	
30	뒤로가기
31	장착