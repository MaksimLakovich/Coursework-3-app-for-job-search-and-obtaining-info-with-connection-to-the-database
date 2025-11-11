import psycopg2

from src.database.abs_table_schema import BaseTableSchema


class CreateTableSchema(BaseTableSchema):
    """Класс-наследник для работы со структурой таблиц в БД PostgreSQL."""

    def __init__(self, database_name: str, params: dict) -> None:
        """Конструктор для подключения к PostgreSQL.
        :param database_name: Название БД.
        :param params: Параметры подключения к БД."""
        self.conn = psycopg2.connect(dbname=database_name, **params)
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    def create_employers_table(self) -> None:
        """Метод для создания таблицы в PostgreSQL для работодателей (Employer)."""
        try:
            self.cur.execute(
                """CREATE TABLE employers (
                employer_id INT PRIMARY KEY,
                employer_name VARCHAR(500) NOT NULL,
                employer_url TEXT
                )
                """)
        except psycopg2.Error as error:
            print(f"❌ Ошибка при создании таблицы employers: {error}")

    def create_vacancies_table(self) -> None:
        """Метод для создания таблицы в PostgreSQL для вакансий (Vacancy)."""
        try:
            self.cur.execute(
                """CREATE TABLE vacancies (
                vacancy_id INT PRIMARY KEY,
                employer_id INT NOT NULL,
                name VARCHAR(500) NOT NULL,
                area_name VARCHAR(500),
                alternate_url TEXT,
                salary_from NUMERIC(10, 2),
                salary_to NUMERIC(10, 2),
                salary_currency VARCHAR(10),
                published_at TIMESTAMP,
                archived BOOL,
                snippet_responsibility TEXT,
                FOREIGN KEY (employer_id) REFERENCES employers(employer_id)
                )
                """)
        except psycopg2.Error as error:
            print(f"❌ Ошибка при создании таблицы vacancies: {error}")

    def close_connection(self) -> None:
        """Метод для закрытия соединения с БД в PostgreSQL."""
        self.cur.close()
        self.conn.close()
