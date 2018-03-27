from django.core.management.base import BaseCommand, CommandError
import requests
from blog.models import Hh_vacancy, Vacancy
import json
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Crowler HH'


    def handle(self, *args, **options):


        null = None
        headers={'User-Agent': 'api-test-agent'}
        key = 'ILSD9A9KV16UCJITR3O7IF843LIPPTUC6AGGQAR389LG0EA83PDMQTQK2HD7DJE6'
        link = 'https://api.hh.ru/vacancies'
        au = 'Bearer ' + key
        headers['Authorization'] = au
        payload = {'text': 'Системный администратор', 'area': '1', 'no_magic': 'true', 'per_page': '100'}
        me = User.objects.get(username='admin')

        def getlink(link, header, payload):
            r = requests.get(link, headers=header, params=payload)
            return r.json()

        data = getlink(link,headers, payload)
        print('Всего страниц ',data['pages'])
        print('Всего вакансий',data['found'])
        pages = data['pages'] + 1

        for page in range(pages):
            print('Сейчас старница №',page)
            payload['page'] = page
            data = getlink(link, headers, payload)
            with open('response.json', 'a', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
            for vacancy1 in data['items']:
                if not Hh_vacancy.objects.filter(vacancy_id=vacancy1['id']):
                    Hh_vacancy.objects.create(author=me,
                                salary_from=(vacancy1.get('salary') or {}).get('from'),
                                salary_to=(vacancy1.get('salary') or {}).get('to'),
                                currency=(vacancy1.get('salary') or {}).get('currency'),
                                gross=(vacancy1.get('salary') or {}).get('gross'),
                                name=vacancy1['name'],
                                area_name=vacancy1['area']['name'],
                                responsibility=vacancy1['snippet']['responsibility'],
                                requirement=vacancy1['snippet']['requirement'],
                                vacancy_id=vacancy1.get('id'),
                                employer_name=(vacancy1.get('employer') or {}).get('id'),
                                employer_id=vacancy1['employer']['name'])
                    data = getlink(vacancy1['url'], headers, payload={})
                    Vacancy.objects.create(vacancy_id=vacancy1.get('id'),
                                            salary_from=(data.get('salary') or {}).get('from'),
                                            salary_to=(data.get('salary') or {}).get('to'),
                                            name=data['name'],
                                            responsibility=data['description'],
                                            requirement=str(data['key_skills']),
                                            experience=data['experience']['name'])

                    with open('response_vacancy.json', 'a', encoding='utf-8') as file:
                        json.dump(data, file, indent=2, ensure_ascii=False)
                else:
                    print('Вакансия уже была')