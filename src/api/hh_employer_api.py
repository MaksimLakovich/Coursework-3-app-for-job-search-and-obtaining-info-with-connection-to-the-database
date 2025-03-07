from typing import List

from src.api.abs_base_employer_api import BaseEmployersAPI
from src.api.base_headhunter_api import HeadHunterBaseAPI


class HeadHunterEmployersAPI(HeadHunterBaseAPI, BaseEmployersAPI):
    """Класс-наследник для поиска ID работодателей по заданному пользователем перечню названий работодателей."""

    def __init__(self) -> None:
        """Конструктор для инициализации подключения к API работодателей (api_name_service = employers)."""
        super().__init__("employers")

    def get_employer_ids(self, employer_names: List[str]) -> List[str]:
        """Метод для выполнения GET-запроса поиска ID работодателя по его названию.
        :param employer_names: Данные настроек пользователя с перечнем названий работодателей в формате dict.
        :return: Список ID работодателей."""
        employer_ids = []
        for name in employer_names:
            params = {"text": name}
            data = self._make_request(params)
            if "items" in data:
                for employer in data["items"]:
                    # Из-за особенностей работы API поиска работодателей в HeadHunter по названию (поле - text), где
                    # параметр text ищет не только точные совпадения, но и ЧАСТИЧНЫЕ. Из-за этого множество лишних
                    # компаний возвращает запрос, которые нам не были нужны совсем. Поэтому нужно добавить фильтрацию
                    # результатов перед добавлением ID в employer_ids (проверяю полностью ли name совпадает с text по
                    # запрашиваемым названием работодателя из пользовательского файла (user_employer_settings.json).
                    if employer["name"].lower() == name.lower():
                        employer_ids.append(employer["id"])
        return employer_ids
