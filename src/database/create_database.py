import psycopg2

from src.database.abs_database_creator import BaseDatabaseCreator


class CreateDatabase(BaseDatabaseCreator):
    """Класс-наследник для работы с базой данных в PostgreSQL."""

    def __init__(self, params: dict) -> None:
        """Конструктор для подключения к PostgreSQL (без выбора БД).
        :param params: Параметры подключения к PostgreSQL."""
        self.conn = psycopg2.connect(dbname="template1", **params)
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    def drop_database(self, database_name: str) -> None:
        """Метод для удаления БД в PostgreSQL, если она существует перед созданием новой.
        :param database_name: Название БД."""
        try:
            # Завершаем активные соединения перед удалением БД, чтоб не было ошибок
            self.cur.execute(
                f"SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = '{database_name}'"
            )
            # Удаляем БД
            self.cur.execute(f"DROP DATABASE IF EXISTS {database_name}")
        except psycopg2.Error as error:
            print(f"❌ Ошибка при удалении базы данных: {error}")

    def create_database(self, database_name: str) -> None:
        """Метод для создания БД в PostgreSQL.
        :param database_name: Название БД."""
        try:
            self.cur.execute(f"CREATE DATABASE {database_name}")
        except psycopg2.Error as error:
            print(f"❌ Ошибка при создании базы данных: {error}")

    def close_connection(self) -> None:
        """Метод для закрытия соединения с PostgreSQL."""
        self.cur.close()
        self.conn.close()
