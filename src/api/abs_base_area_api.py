from abc import ABC, abstractmethod


class BaseAreasAPI(ABC):
    """Абстрактный класс для работы с API регионов/городов."""

    @abstractmethod
    def get_area_ids(self, area_names: list) -> list:
        """Абстрактный метод для поиска ID регионов/городов по заданному пользователем перечню названий городов.
        :param area_names: Список городов, заданных пользователем.
        :return: Список ID городов."""
        pass
