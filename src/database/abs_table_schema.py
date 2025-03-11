from abc import ABC, abstractmethod


class BaseTableSchema(ABC):
    """Абстрактный класс для работы со структурой таблиц в БД."""

    @abstractmethod
    def __init__(self):
        """Конструктор для подключения к Database."""
        pass

    @abstractmethod
    def create_employers_table(self):
        """Абстрактный метод для создания в БД таблицы для работодателей (Employer)."""
        pass

    @abstractmethod
    def create_vacancies_table(self):
        """Абстрактный метод для создания в БД таблицы для вакансий (Vacancy)."""
        pass
