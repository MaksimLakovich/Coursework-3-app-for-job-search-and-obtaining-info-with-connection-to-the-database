from abc import ABC, abstractmethod


class BaseTableFiller(ABC):
    """Абстрактный класс для работы с содержимым таблиц в БД (загрузка данных)."""

    @abstractmethod
    def fill_employers_table(self, json_file: str):
        """Абстрактный метод для загрузки данных о работодателях.
        :param json_file: Путь к JSON-файлу с данными."""
        pass

    @abstractmethod
    def fill_vacancies_table(self, json_file: str):
        """Абстрактный метод для загрузки данных о вакансиях.
        :param json_file: Путь к JSON-файлу с данными."""
        pass
