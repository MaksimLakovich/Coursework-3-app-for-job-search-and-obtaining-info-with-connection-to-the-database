from typing import Any, Dict, List

import psycopg2

from src.database.abs_table_filler import BaseTableFiller


class FillTable(BaseTableFiller):
    """Класс-наследник для работы с содержимым таблиц в БД PostgreSQL (загрузка данных)."""

    def __init__(self, database_name: str, params: dict) -> None:
        """Конструктор для подключения к PostgreSQL.
        :param database_name: Название БД.
        :param params: Параметры подключения."""
        self.conn = psycopg2.connect(dbname=database_name, **params)
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    def fill_employers_table(self, json_data: List[Dict[str, Any]]) -> None:
        """Метод для загрузки данных о работодателях в таблицу 'employers' в БД PostgreSQL.
        :param json_data: Данные о работодателях."""
        try:
            for employer in json_data:
                employer_id = employer.get("employer_id")
                employer_name = employer.get("employer_name")
                employer_url = employer.get("employer_url")

                if employer_id and employer_name:  # Проверяю, есть ли обязательные поля
                    self.cur.execute(
                        """
                        INSERT INTO employers (employer_id, employer_name, employer_url)
                        VALUES (%s, %s, %s)
                        """,
                        (employer_id, employer_name, employer_url)
                    )

        except psycopg2.Error as error:
            print(f"❌ Ошибка при загрузке данных в таблицу 'employers': {error}")

    def fill_vacancies_table(self, json_data: List[Dict[str, Any]]) -> None:
        """Метод для загрузки данных о вакансиях в таблицу 'vacancies' в БД PostgreSQL.
        :param json_data: Данные о вакансиях."""
        try:
            for vacancy in json_data:
                vacancy_id = vacancy.get("vacancy_id")
                employer_id = vacancy.get("employer_id")
                name = vacancy.get("name")
                area_name = vacancy.get("area_name")
                alternate_url = vacancy.get("alternate_url")
                salary_from = vacancy.get("salary_from")
                salary_to = vacancy.get("salary_to")
                salary_currency = vacancy.get("salary_currency")
                published_at = vacancy.get("published_at")
                archived = vacancy.get("archived")
                snippet_responsibility = vacancy.get("snippet_responsibility")

                if vacancy_id and name and employer_id:
                    self.cur.execute(
                        """
                        INSERT INTO vacancies (vacancy_id, employer_id, name, area_name, alternate_url, salary_from, 
                        salary_to, salary_currency, published_at, archived, snippet_responsibility)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """,
                        (vacancy_id, employer_id, name, area_name, alternate_url, salary_from, salary_to,
                         salary_currency, published_at, archived, snippet_responsibility)
                    )

        except psycopg2.Error as error:
            print(f"❌ Ошибка при загрузке данных в таблицу 'vacancies': {error}")

    def close_connection(self) -> None:
        """Метод для закрытия соединения с БД в PostgreSQL."""
        self.cur.close()
        self.conn.close()
