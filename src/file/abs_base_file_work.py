from abc import ABC, abstractmethod
from pathlib import Path


class BaseFileWork(ABC):
    """Абстрактный класс BaseFileWork для работы с файлами."""

    @abstractmethod
    def __init__(self, path_to_file: Path) -> None:
        """Конструктор для инициализации пути к файлу, который будет хранить результаты выгрузки данных.
        :param path_to_file: Путь к файлу (JSON, CSV и т.д.)."""
        pass
