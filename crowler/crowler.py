import json
import requests 

text = 'системный администратор Москва'
link = 'https://api.hh.ru/vacancies?text=%s' % text
r = requests.get(link, headers={'User-Agent': 'api-test-agent'})
data = r.json()
with open('response.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)