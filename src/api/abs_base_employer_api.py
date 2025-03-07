from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseEmployersAPI(ABC):
    """Абстрактный класс для работы с API работодателей."""

    @abstractmethod
    def get_employer_ids(self, employer_names: Dict[str, Any]) -> list:
        """Абстрактный метод для поиска ID работодателей по заданному пользователем перечню названий работодателей.
        :param employer_names: Данные настроек пользователя с перечнем названий работодателей в формате dict.
        :return: Список ID работодателей."""
        pass
