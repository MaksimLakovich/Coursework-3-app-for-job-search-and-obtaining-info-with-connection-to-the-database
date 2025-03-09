import json
from pathlib import Path
from typing import Union

from config import file_with_employers, file_with_vacancies, initialize_directories
from src.employer_to_dict import employer_to_dict
from src.file.abs_base_file_work import BaseFileWork
from src.objects.employer import Employer
from src.objects.vacancy import Vacancy
from src.vacancy_to_dict import vacancy_to_dict


class JSONSaver(BaseFileWork):
    """Класс-наследник от абстрактного класса (BaseFileWork) для работы с JSON-файлами (вакансии и работодатели)."""

    def __init__(
            self,
            path_to_file_vacancies: Path = file_with_vacancies,
            path_to_file_employers: Path = file_with_employers
    ) -> None:
        """Конструктор для инициализации путей к JSON-файлам, которые будут хранить данные о вакансиях и работодателях.
        :param path_to_file_vacancies: Путь к JSON-файлу с вакансиями.
        :param path_to_file_employers: Путь к JSON-файлу с работодателями."""
        initialize_directories()  # Создаю директорию и файл доп функцией initialize_directories(), если этого еще нет
        self.__file_with_vacancies = file_with_vacancies

    def add_vacancy(self, vacancies: Union["Vacancy", list["Vacancy"]]) -> None:
        """Метод для добавления вакансий в JSON-файл.
        :param vacancies: Список объектов Vacancy, содержащих данные о вакансиях."""
        vacancies_data = []
        if not isinstance(vacancies, list):  # Если передан один объект, преобразовываю его в список
            vacancies = [vacancies]
        for vacancy in vacancies:  # Преобразую объекты Vacancy в список словарей
            vacancies_data.append(vacancy_to_dict(vacancy))
        with open(self.__file_with_vacancies, "w", encoding="utf-8") as file:  # Записываю результат в JSON-файл
            json.dump(vacancies_data, file, indent=4, ensure_ascii=False)
        print(f"✅ JSON-файл с вакансиями перезаписан ({len(vacancies_data)} вакансий)")

    def add_employer(self, vacancies: list[Vacancy]) -> None:
        """Метод для добавления работодателей в JSON-файл.
        :param vacancies: Список объектов Vacancy, содержащих данные о работодателях."""
        employers_data = []
        # Извлекаю работодателей без дубликатов
        employers = {
            v.employer_id: Employer(v.employer_id, v.employer_name, v.employer_url)
            for v in vacancies
        }
        for employer in employers.values():  # Преобразовываю объекты Employer в список словарей
            employers_data.append(employer_to_dict(employer))
        with open("data/json_data_employers.json", "w", encoding="utf-8") as file:  # Записываю результат в JSON-файл
            json.dump(employers_data, file, indent=4, ensure_ascii=False)

        print(f"✅ JSON-файл с работодателями перезаписан ({len(employers_data)} записей)")
