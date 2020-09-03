# https://www.linuxuprising.com/2020/02/how-to-keep-onedrive-in-sync-with.html

pkill -f onedrive
onedrive --synchronize --resync
onedrive -m

# 계속동기화
 systemctl --user enable onedrive
 systemctl --user start onedrive
 systemctl --user restart onedrive


 systemctl --user stop onedrive
 pkill -f onedrive
# 상태확인
 systemctl status --user onedrive
# 로그확인
journalctl --user-unit onedrive -f

onedrive  --synchronize --download-only
onedrive  --synchronize --upload-only
