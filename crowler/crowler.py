from db import db_session, Hh_vacancy, Vacancy
import json
import requests

h = Hh_vacancy
null = None
text = 'Системный+администратор'
link = 'https://api.hh.ru/vacancies?text={0}&area=1&no_magic=true&per_page=100'.format(text)
headers={'User-Agent': 'api-test-agent'}
key = ''
au = 'Bearer ' + key
headers['Authorization'] = au

r = requests.get(link, headers)
data = r.json()
print(data['pages'])
print(data['found'])
pages = data['pages'] + 1

for page in range(pages):
    link = 'https://api.hh.ru/vacancies?text={1}&area=1&page={0}&per_page=100'.format(page, text)
    print(page)
    r = requests.get(link, headers={'User-Agent': 'api-test-agent'})
    data = r.json()
    with open('response.json', 'a', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    for vacancy in data['items']:
        try:
            hh_vacancy = Hh_vacancy(vacancy['salary']['from'], vacancy['salary']['to'], vacancy['salary']['currency'], vacancy['salary']['gross'], vacancy['name'], vacancy['area']['name'], vacancy['snippet']['responsibility'], vacancy['snippet']['requirement'],vacancy.setdefault('employer').setdefault('id'), vacancy['employer']['name'])
        except TypeError:
            print('Не указана зарплата')
            hh_vacancy = Hh_vacancy(None, None, None, None, vacancy['name'], vacancy['area']['name'], vacancy['snippet']['responsibility'], vacancy['snippet']['requirement'], vacancy['id'], vacancy.setdefault('employer').setdefault('id'), vacancy['employer']['name'])
        db_session.add(hh_vacancy)
        db_session.commit()
        hh_id = h.query.filter(Hh_vacancy.vacancy_id == vacancy['id']).first()
        url = vacancy['url']
        r = requests.get(url, headers={'User-Agent': 'api-test-agent'})
        data = r.json()
        try:
            vacancy1 = Vacancy(data['salary']['from'], data['salary']['to'], data['name'], data['description'], str(data['key_skills']), data['experience']['name'], hh_id.id)
        except TypeError:
            print('Не указана зарплата')
            vacancy1 = Vacancy(None, None, data['name'], data['description'], str(data.setdefault('key_skills')), data.setdefault('experience').setdefault('name'), hh_id.id)
        db_session.add(vacancy1)
        db_session.commit()
        with open('response_vacancy.json', 'a', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

