import psycopg2

from src.db_manager.abs_database_manager import BaseDBManager


class DBManager(BaseDBManager):
    """Класс-наследник для пользовательского взаимодействия с БД в PostgreSQL."""

    def __init__(self, database_name: str, params: dict) -> None:
        """Конструктор для подключения к БД в PostgreSQL.
        :param database_name: Название БД.
        :param params: Параметры подключения к БД."""
        self.conn = psycopg2.connect(dbname=database_name, **params)
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self) -> list[tuple]:
        """Метод для получения списка всех компаний и количества вакансий у каждой компании."""
        try:
            self.cur.execute(
                """
                SELECT employers.employer_name, COUNT(vacancies.vacancy_id)
                FROM vacancies
                JOIN employers USING(employer_id)
                GROUP BY employers.employer_name
                """
            )
            query_result = self.cur.fetchall()  # Получаю все данные из курсора для будущей печати
            return query_result
        except psycopg2.Error as error:
            print(f"❌ Ошибка при выполнении запроса: {error}.")
            return []

    def get_all_vacancies(self) -> list[tuple]:
        """Метод для получения списка всех вакансий с указанием названия компании, названия вакансии, зарплаты и
        ссылки на вакансию."""
        try:
            self.cur.execute(
                """
                SELECT employers.employer_name, vacancies.name, vacancies.salary_from,
                vacancies.salary_to, vacancies.alternate_url
                FROM vacancies
                JOIN employers USING(employer_id)
                ORDER BY vacancies.name
                """
            )
            query_result = self.cur.fetchall()
            return query_result
        except psycopg2.Error as error:
            print(f"❌ Ошибка при выполнении запроса: {error}.")
            return []

    def get_avg_salary(self) -> list[tuple]:
        """Метод для получения средней зарплаты по вакансиям."""
        try:
            self.cur.execute(
                """
                SELECT employers.employer_name,
                AVG(NULLIF(salary_from, 0)) AS avg_salary_from  -- Игнорирую нулевые зарплаты
                FROM vacancies
                JOIN employers USING(employer_id)
                GROUP BY employers.employer_name
                """
            )
            query_result = self.cur.fetchall()
            return query_result
        except psycopg2.Error as error:
            print(f"❌ Ошибка при выполнении запроса: {error}.")
            return []

    def get_vacancies_with_higher_salary(self) -> list[tuple]:
        """Метод для получения списка всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        try:
            self.cur.execute(
                """
                SELECT *
                FROM vacancies
                WHERE salary_from > (SELECT AVG(salary_from)
                FROM vacancies
                WHERE salary_from > 0)
                ORDER BY salary_from
                """
            )
            query_result = self.cur.fetchall()
            return query_result
        except psycopg2.Error as error:
            print(f"❌ Ошибка при выполнении запроса: {error}.")
            return []

    def get_vacancies_with_keyword(self, keyword: str) -> list[tuple]:
        """Метод для получения списка всех вакансий, в названии и описании которых есть переданные в метод слова.
        :param keyword: Ключевое слово для поиска."""
        try:
            self.cur.execute(
                """
                SELECT vacancy_id, employer_id, name, area_name, alternate_url,
                salary_from, salary_to, salary_currency, published_at, archived, snippet_responsibility
                FROM vacancies
                WHERE name ILIKE %s OR snippet_responsibility ILIKE %s
                ORDER BY published_at DESC
                """,
                (f"%{keyword}%", f"%{keyword}%")  # Поиск и в названии и в описании
            )
            query_result = self.cur.fetchall()
            return query_result
        except psycopg2.Error as error:
            print(f"❌ Ошибка при выполнении запроса: {error}.")
            return []

    def close_connection(self) -> None:
        """Метод для закрытия соединения с БД в PostgreSQL."""
        self.cur.close()
        self.conn.close()
