from typing import Any, Dict, Mapping

import requests


class HeadHunterBaseAPI():
    """Базовый класс для работы с API сервиса HeadHunter."""

    BASE_HEADHUNTER_URL = "https://api.hh.ru"

    def __init__(self, api_name_service: str) -> None:
        """Конструктор для инициализации подключения к API сервиса.
        :param api_name_service: Значение 'employers' или 'vacancies' для формирования url сервиса HeadHunter."""
        self._url = f"{self.BASE_HEADHUNTER_URL}/{api_name_service}"
        self._headers = {"User-Agent": "HH-User-Agent"}

    def _make_request(self, params: Mapping[str, Any]) -> Dict[str, Any]:
        """Метод для выполнения GET-запросов.
        :param params: Параметры запросов (либо для 'employers', либо для 'vacancies')."""
        try:
            response = requests.get(self._url, headers=self._headers, params=params)
            response.raise_for_status()  # Если код 4xx или 5xx, то выбрасывается исключение
            return response.json()
        except requests.exceptions.RequestException as info:
            print(f"❌Ошибка при обращении к API hh.ru: {info}")
            return {}
