from abc import ABC, abstractmethod
from typing import Any, Dict, List


class BaseVacanciesAPI(ABC):
    """Абстрактный класс для работы с API вакансий."""

    @abstractmethod
    def get_vacancies(self, keyword: str, employer_ids: List[str], area_ids: List[int]) -> List[Dict[str, Any]]:
        """Абстрактный метод для поиска вакансий по ID работодателей.
        :param keyword: Ключевое слово для поиска.
        :param employer_ids: Список ID работодателей.
        :param area_ids: Список ID регионов/городов.
        :return: Список с данными о работодателях и их вакансиях."""
        pass
