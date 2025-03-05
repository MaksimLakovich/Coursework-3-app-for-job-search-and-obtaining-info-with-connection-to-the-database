from typing import Any

import requests

from src.abs_base_api import BaseAPI


class HeadHunterAPI(BaseAPI):
    """Класс-наследник от абстрактного класса (BaseAPI) для работы с платформой hh.ru."""

    def __init__(self) -> None:
        """Конструктор для инициализации подключения к API сервису."""
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params: dict[str, str | int] = {"employer_id": "", "page": 0, "per_page": 100}
        self.__vacancies: list[dict[str, Any]] = []  # Итоговый список, в который складываются найденные вакансии.

    def load_vacancies(self, employers: list) -> list[dict[str, Any]]:
        """Метод для получения работодателей и вакансии с API сервиса HeadHunter.ru по заданному списку работодателей.
        :param employers: Список работодателей для получения данных об их вакансиях.
        :return: Список с данными о работодателях и их вакансиях."""

        # Устанавливаю в .........self.params['text'] конструктора класса значение .................=keyword (ключевое слово или фраза), которое
        # будет искаться в ................специальных полях вакансии
        self.__params["employer_id"] = employers
        # При указании параметров пагинации (page, per_page) работает ограничение: глубина возвращаемых результатов
        # не может быть больше 2000, поэтому прохожу циклом по 20 страницам (от 0 до 19)
        while self.__params.get("page") != 1:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            if response.status_code == 200:
                try:
                    vacancies = response.json()["items"]  # Сохранение в переменную 'vacancies' найденных на странице вакансий из items
                    self.__vacancies.extend(vacancies)  # Добавление в общий список 'self.__vacancies' всех вакансий из переменной 'vacancies'
                    self.__params["page"] += 1  # Переход на следующую страницу
                except requests.exceptions.RequestException as info:
                    print(f"❌Ошибка при обращении к API hh.ru: {info}")
                    return []
                except KeyError:
                    print("❌Некорректный формат ответа API hh.ru.")
                    return []
            else:
                print(f"❌Ошибка: {response.status_code}, текст: {response.text}")
                return []
        return self.__vacancies
