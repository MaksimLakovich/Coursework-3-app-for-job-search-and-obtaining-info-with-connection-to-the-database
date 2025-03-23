from abc import ABC, abstractmethod


class BaseTableSchema(ABC):
    """Абстрактный класс для работы со структурой таблиц в БД."""

    def __init__(self, database_name: str, params: dict) -> None:
        """Конструктор для подключения к БД.
        :param database_name: Название БД.
        :param params: Параметры подключения к БД."""
        pass

    @abstractmethod
    def create_employers_table(self) -> None:
        """Абстрактный метод для создания таблицы для работодателей (Employer)."""
        pass

    @abstractmethod
    def create_vacancies_table(self) -> None:
        """Абстрактный метод для создания таблицы для вакансий (Vacancy)."""
        pass

    def close_connection(self) -> None:
        """Абстрактный метод для закрытия соединения с БД."""
        pass
