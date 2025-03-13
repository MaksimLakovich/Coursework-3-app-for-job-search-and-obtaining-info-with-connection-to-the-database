from abc import ABC, abstractmethod


class BaseDatabaseCreator(ABC):
    """Абстрактный класс для работы с базой данных."""

    @abstractmethod
    def __init__(self, params: dict) -> None:
        """Конструктор для подключения к БД.
        :param params: Параметры подключения к БД."""
        pass

    @abstractmethod
    def drop_database(self, database_name: str) -> None:
        """Абстрактный метод для удаления БД перед созданием новой.
        :param database_name: Название БД."""
        pass

    @abstractmethod
    def create_database(self, database_name: str) -> None:
        """Абстрактный метод для создания БД.
        :param database_name: Название БД."""
        pass

    def close_connection(self) -> None:
        """Абстрактный метод для закрытия соединения с БД."""
        pass
