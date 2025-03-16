from pathlib import Path

from config import (config, file_with_employers, file_with_vacancies,
                    path_to_user_employer_settings)
from src.api.hh_area_api import HeadHunterAreasAPI
from src.api.hh_employer_api import HeadHunterEmployersAPI
from src.api.hh_vacancy_api import HeadHunterVacanciesAPI
from src.database.create_database import CreateDatabase
from src.database.create_table_schema import CreateTableSchema
from src.database.fill_table import FillTable
from src.file.json_file_work import JSONSaver
from src.objects.vacancy import Vacancy
from src.read_file_with_employer_names import read_json_user_employer_settings
from src.read_json_data_employers import read_json_data_employers
from src.read_json_data_vacancies import read_json_data_vacancies


def user_interaction(
    path_to_settings: Path, path_to_file_employers: Path, path_to_file_vacancies: Path
) -> None:
    """Функция для взаимодействия пользователя с программой.
    :param path_to_settings: Путь к JSON-файлу с пользовательскими настройками со списком работодателей (10 компаний).
    :param path_to_file_employers: Путь к JSON-файлу с работодателями.
    :param path_to_file_vacancies: Путь к JSON-файлу с вакансиями."""

    employers_list = read_json_user_employer_settings(path_to_settings)["employer_names"]
    area_name = ["Все города"]
    search_text = "Не задано"

    while True:
        print("🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹")
        print(f"🚀 Текущий список компаний: {employers_list}")
        print(f"🚀 Текущий список городов: {area_name}")
        print(f"🚀 Текущий список ключевых слов: {search_text}")
        print("🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹")
        print("\nУстановите дополнительные параметры поиска вакансий и работодателей:")
        print("1️⃣ - ЗАПУСТИТЬ ПОИСК ПО ЗАДАННЫМ ПАРАМЕТРАМ")
        print("2️⃣ - (❌не реализовано) Изменить текущий список компаний в поиске")
        print("3️⃣ - Изменить список городов в поиске вакансий")
        print("4️⃣ - Задать ключевое слово в поиске вакансий")
        print("5️⃣ - Сбросить дополнительные параметры и вернуться к настройкам по умолчанию")
        print("6️⃣ - Выход из программы")
        choice = input("Выберите действие (1-6): ").strip()

        if choice == "1":

            platforms = ["HeadHunter"]  # Сейчас это только "HeadHunter", но в будущем можно добавить другие сервисы

            while True:
                select_platform = input(f"\nВыберите платформу для поиска вакансий ({', '.join(platforms)}): ").strip()
                if select_platform.lower() == "headhunter":  # Проверяем без учета регистра
                    select_platform = "HeadHunter"  # Потом присваиваем правильное название
                    print(f"✅ Выбрана платформа: {select_platform}")
                    break
                else:
                    print(f"❌ Ошибка: Платформа '{select_platform}' не поддерживается. Введите платформу из списка.")

            # Подключение к HeadHunter
            if select_platform == "HeadHunter":

                # Создаем экземпляр класса для работы с API работодателей и получаем список ID работодателей
                hh_employer_api = HeadHunterEmployersAPI()
                hh_list_employer_ids = hh_employer_api.get_employer_ids(employers_list)

                # Создаем экземпляр класса для работы с API регионов/городов и получаем список ID городов
                hh_area_api = HeadHunterAreasAPI()
                hh_list_area_ids = hh_area_api.get_area_ids(area_name)

                # Создаем экземпляр класса для работы с API вакансий и получаем все вакансии по заданным условиям:
                # 1) по указанному списку компаний (работодателей)
                # 2) по указанному списку городов
                # 3) по указанному ключевому слову
                hh_vacancy_api = HeadHunterVacanciesAPI()
                if search_text == "Не задано":
                    search_text = ""
                    hh_list_vacancies = hh_vacancy_api.get_vacancies(
                        search_text, hh_list_employer_ids, hh_list_area_ids
                    )
                else:
                    hh_list_vacancies = hh_vacancy_api.get_vacancies(
                        search_text, hh_list_employer_ids, hh_list_area_ids
                    )

                # Изменяем полученные данные с API в список объектов Vacancy
                vacancies_data = Vacancy.cast_to_object_list(hh_list_vacancies)

                # Сохраняем полученные данные о вакансиях и работодателях в JSON-файлы
                json_saver_for_vacancy = JSONSaver()
                json_saver_for_vacancy.add_vacancy(vacancies_data)
                json_saver_for_vacancy.add_employer(vacancies_data)

                # Создаем и сохраняем данные о вакансиях и работодателях в БД
                my_database_name = "coursework_3_database_vacancy"
                # Используем функцию для парсинга параметров подключения к БД из database.ini
                params = config()

                # ШАГ 1: Создаем экземпляр класса для работы с Database
                bd_postgresql = CreateDatabase(params)
                # Создаем базу данных в PostgreSQL
                bd_postgresql.drop_database(my_database_name)
                bd_postgresql.create_database(my_database_name)
                bd_postgresql.close_connection()  # Закрываем соединения с БД, чтоб не было с ней потом проблем

                # ШАГ 2: Создаем экземпляр класса для работы с таблицами
                table_postgresql = CreateTableSchema(my_database_name, params)
                # Создаем таблицы в PostgreSQL
                table_postgresql.create_employers_table()
                table_postgresql.create_vacancies_table()
                table_postgresql.close_connection()  # Закрываем соединения с БД, чтоб не было с ней потом проблем

                # ШАГ 3: Создаем экземпляр класса для работы с содержимым таблиц в БД PostgreSQL
                fill_table_postgresql = FillTable(my_database_name, params)
                # Получаем данные из json-файлов
                employers_data = read_json_data_employers(path_to_file_employers)
                vacancies_data = read_json_data_vacancies(path_to_file_vacancies)
                # Загружаем данные из JSON-файлов в таблицы
                fill_table_postgresql.fill_employers_table(employers_data)
                fill_table_postgresql.fill_vacancies_table(vacancies_data)
                fill_table_postgresql.close_connection()  # Закрываем соединения с БД, чтоб не было с ней потом проблем

        elif choice == "2":
            print("❌ Изменение списка компаний пока не реализовано.")

        elif choice == "3":

            user_choice = (input("Введите город (или набор городов через запятую): ").title())

            if area_name[0] == "Все города":
                area_name = []  # Очищаю список, так как пользователь вводит новые города и нужно удалить "Все города"
                for city in user_choice.split(","):
                    area_name.append(city.strip())  # Добавляю каждый город отдельно
            else:
                for city in user_choice.split(","):
                    area_name.append(city.strip())  # Добавляю новые города в существующий список городов

        elif choice == "4":

            user_choice = (input("Введите ключевое слово: ").strip().lower())
            search_text = user_choice

        elif choice == "5":
            employers_list = read_json_user_employer_settings(path_to_settings)["employer_names"]
            area_name = ["Все города"]
            search_text = "Не задано"
            print("✅Дополнительные параметры сброшены и возвращены настройки по умолчанию.")

        elif choice == "6":
            print("✅Завершение работы.")
            break

        else:
            print("❌Ошибка: Некорректный ввод. Попробуйте снова.")


if __name__ == "__main__":
    user_interaction(
        path_to_user_employer_settings, file_with_employers, file_with_vacancies
    )
