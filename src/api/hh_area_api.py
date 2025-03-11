from typing import List

from src.api.abs_base_area_api import BaseAreasAPI
from src.api.base_headhunter_api import HeadHunterBaseAPI


class HeadHunterAreasAPI(HeadHunterBaseAPI, BaseAreasAPI):
    """Класс-наследник для поиска ID городов по заданному пользователем перечню названий городов."""

    def __init__(self) -> None:
        """Конструктор для инициализации подключения к API регионов/городов (api_name_service = areas)."""
        super().__init__("areas")

    def get_area_ids(self, area_names: List[str]) -> List[int]:
        """Метод для выполнения GET-запроса поиска ID городов по их названию.
        :param area_names: Список городов, заданных пользователем.
        :return: Список ID городов."""
        area_ids: List[int] = []

        # 1) Запрашиваю данные о регионах через наш "_make_request()"; 2) "areas API" не требует никаких параметров,
        # судя по документации, поэтому получаем все, а потом выполняем поиск наших городов
        data = self._make_request({})

        if not data or not isinstance(data, list):  # Проверяю, что API вернул список стран
            print("❌ Ошибка: Не удалось получить список городов, будут возвращены все города по умолчанию.")
            return [1]  # Если API вернул пустой ответ, то использую ID для "Все города"

        for country in data:  # Перебираю страны
            for region in country["areas"]:  # Перебираю регионы
                for city in region["areas"]:  # Перебираю города
                    if city["name"].lower() in [name.lower() for name in area_names]:
                        area_ids.append(int(city["id"]))

        return area_ids if area_ids else [1]  # Если ничего не найдено, то использую ID для "Все города"
