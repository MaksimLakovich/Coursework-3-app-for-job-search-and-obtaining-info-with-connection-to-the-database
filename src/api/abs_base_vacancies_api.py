from abc import ABC, abstractmethod
from typing import Any


class BaseVacanciesAPI(ABC):
    """Абстрактный класс для работы с API вакансий."""

    @abstractmethod
    def get_vacancies(self, employer_ids: list) -> list[dict[str, Any]]:
        """Абстрактный метод для поиска вакансий по ID работодателей.
        :param employer_ids: Список ID работодателей.
        :return: Список с данными о работодателях и их вакансиях."""
        pass
