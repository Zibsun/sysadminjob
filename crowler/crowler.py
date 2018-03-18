from db import db_session, Hh_vacancy, Vacancy
import json
import requests
import sqlite3
h = Hh_vacancy
null = None
headers={'User-Agent': 'api-test-agent'}
key = ''
link = 'https://api.hh.ru/vacancies'
au = 'Bearer ' + key
headers['Authorization'] = au
payload = {'text': 'Системный администратор', 'area': '1', 'no_magic': 'true', 'per_page': '100'}


def getlink(link, header, payload):
    r = requests.get(link, headers=header, params=payload)
    return r.json()

data = getlink(link,headers, payload)
print(data['pages'])
print(data['found'])
pages = data['pages'] + 1

for page in range(pages):
    print(page)
    payload['page'] = page
    data = getlink(link, headers, payload)
    with open('response.json', 'a', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    for vacancy in data['items']:
        if not h.query.filter(Hh_vacancy.vacancy_id == vacancy['id']).first():
            hh_vacancy = Hh_vacancy((vacancy.get('salary') or {}).get('from'),
                                (vacancy.get('salary') or {}).get('to'),
                                (vacancy.get('salary') or {}).get('currency'),
                                (vacancy.get('salary') or {}).get('gross'),
                                vacancy['name'], vacancy['area']['name'],
                                vacancy['snippet']['responsibility'],
                                vacancy['snippet']['requirement'],
                                vacancy.get('id'),
                                (vacancy.get('employer') or {}).get('id'),
                                vacancy['employer']['name'])

            db_session.add(hh_vacancy)
            db_session.commit()
            hh_id = h.query.filter(Hh_vacancy.vacancy_id == vacancy['id']).first()
            data = getlink(vacancy['url'], headers, payload={})
            get_salary = data.get('salary', {})
            vacancy1 = Vacancy((data.get('salary') or {}).get('from'),
                            (data.get('salary') or {}).get('to'),
                            data['name'],
                            data['description'],
                            str(data['key_skills']),
                            data['experience']['name'],
                            hh_id.id)
            db_session.add(vacancy1)
            db_session.commit()
            with open('response_vacancy.json', 'a', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
        else:
            print('Вакансия уже была')
