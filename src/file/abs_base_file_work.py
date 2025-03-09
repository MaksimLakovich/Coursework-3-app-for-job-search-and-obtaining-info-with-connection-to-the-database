from abc import ABC, abstractmethod
from pathlib import Path


class BaseFileWork(ABC):
    """Абстрактный класс BaseFileWork для работы с файлами."""

    @abstractmethod
    def __init__(self, path_to_file_vacancies: Path, path_to_file_employers: Path) -> None:
        """Конструктор для инициализации путей к файлам, которые будут хранить результаты выгрузки данных.
        :param path_to_file_vacancies: Путь к файлу с вакансиями (JSON, CSV и т.д.).
        :param path_to_file_employers: Путь к файлу с работодателями (JSON, CSV и т.д.)."""
        pass
