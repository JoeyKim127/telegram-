import requests
from pprint import pprint as pp
from decouple import config


chat_id = ''
text = ''
base_url = 'https://api.telegram.org'
token = config('TOKEN')
print(token)


url = f'{base_url}/bot{token}/getUpdates'
print(url)

res = requests.get(url)
print(res)

data = res.json()
# pp(data)


sender = []

pp(data["result"][-1]["message"]['chat']['id'])
print("here")
# sender.append(data["result"][-1]["message"]['chat']['id'])
sender = data["result"][-1]["message"]['chat']['id']
print(sender)


chat_id = 'sender'
text = 'Python으로 메세지 보내기 성공'
base_url = 'https://api.telegram.org'
token = config('TOKEN')


url = f'{base_url}/bot{token}/sendMessage?chat_id={sender}&text={text}'
print(url)
