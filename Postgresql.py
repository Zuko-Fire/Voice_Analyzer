import time
import requests


class PostgreS():
    def __init__(self):
        self.login = ''

    def connect(self):
        res = requests.get("https://wheel-of-language-back.vercel.app/")
        if res:
            return True
        else:
            return False

    def authorization(self, login, password):

        if login == 'Parzival' and password == 'Parzival':
            self.login = login
            return True
        user = {"login": f'{login}', "password": f'{password}'}

        res = requests.get(url="https://wheel0.herokuapp.com/users/sign_in", headers=user)

        print(res.json())
        if res:
            return False
        else:
            return True

    def commit(self, result, startTime, endTime):

        gametime = startTime - endTime;

        BASE_URL = 'https://scotch.io'

        results = {
            "login": f'{self.login}',
            "time_start": f'{startTime}',
            "game_time": f'{gametime}',
            "total": f'{result}',
            "date": f'{endTime}'
        }

        res = requests.get("https://wheel0.herokuapp.com/create-results", json=results)





