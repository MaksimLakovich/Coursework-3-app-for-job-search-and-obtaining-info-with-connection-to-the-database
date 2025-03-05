from abc import ABC, abstractmethod
from typing import Any


class BaseAPI(ABC):
    """Абстрактный класс BaseAPI для работы с API сервисов с работодателями и вакансиями."""

    @abstractmethod
    def __init__(self) -> None:
        """Конструктор для инициализации подключения к API сервису."""
        pass

    @abstractmethod
    def load_vacancies(self, employers: list) -> list[dict[str, Any]]:
        """Метод для получения работодателей и вакансии с API сервиса по заданному списку работодателей.
        :param employers: Список работодателей для получения данных об их вакансиях.
        :return: Список с данными о работодателях и их вакансиях."""
        pass
