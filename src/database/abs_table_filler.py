from abc import ABC, abstractmethod
from typing import Any, Dict, List


class BaseTableFiller(ABC):
    """Абстрактный класс для работы с содержимым таблиц в БД (загрузка данных)."""

    @abstractmethod
    def __init__(self, database_name: str, params: dict) -> None:
        """Конструктор для подключения к БД.
        :param database_name: Название БД.
        :param params: Параметры подключения к БД."""
        pass

    @abstractmethod
    def fill_employers_table(self, json_data: List[Dict[str, Any]]) -> None:
        """Абстрактный метод для загрузки данных о работодателях в таблицу БД.
        :param json_data: Данные о работодателях."""
        pass

    @abstractmethod
    def fill_vacancies_table(self, json_data: List[Dict[str, Any]]) -> None:
        """Абстрактный метод для загрузки данных о вакансиях в таблицу БД.
        :param json_data: Данные о работодателях."""
        pass

    def close_connection(self) -> None:
        """Абстрактный метод для закрытия соединения с БД."""
        pass
