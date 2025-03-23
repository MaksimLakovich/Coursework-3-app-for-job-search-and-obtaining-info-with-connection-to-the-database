from abc import ABC, abstractmethod
from typing import List


class BaseEmployersAPI(ABC):
    """Абстрактный класс для работы с API работодателей."""

    @abstractmethod
    def get_employer_ids(self, employer_names: List[str]) -> List[str]:
        """Абстрактный метод для поиска ID работодателей по заданному пользователем перечню названий работодателей.
        :param employer_names: Данные настроек пользователя с перечнем названий работодателей.
        :return: Список ID работодателей."""
        pass
