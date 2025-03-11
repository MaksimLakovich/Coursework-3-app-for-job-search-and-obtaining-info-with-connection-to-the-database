from abc import ABC, abstractmethod


class BaseDatabaseCreator(ABC):
    """Абстрактный класс для работы с базой данных."""

    @abstractmethod
    def __init__(self):
        """Конструктор для инициализации/создания Database."""
        pass

    @abstractmethod
    def drop_database(self) -> bool:
        """Абстрактный метод для удаления БД перед созданием новой."""
        pass
