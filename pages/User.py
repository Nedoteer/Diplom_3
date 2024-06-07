import string
import random

import allure
import requests

from data import StellarData
from urls import Urls


class User:
    @staticmethod
    @allure.step('Генерация рандомных значений')
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @allure.step('Создание пользователя')
    def create_user(self):
        us = self.generate_random_string(5)
        payload = {"email": f'{us}@yopmail.com',
                   "password": "password",
                   "name": "Username"
                   }
        login = {
            "email": f'{us}@yopmail.com',
            "password": "password"
        }
        response = requests.post(Urls.STELLAR + Urls.URL_REGISTER, json=payload)

        return response


