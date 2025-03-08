from typing import Any, Dict, List

from src.api.abs_base_vacancies_api import BaseVacanciesAPI
from src.api.base_headhunter_api import HeadHunterBaseAPI


class HeadHunterVacanciesAPI(HeadHunterBaseAPI, BaseVacanciesAPI):
    """Класс-наследник для поиска вакансий по переданному списку ID работодателей."""

    def __init__(self) -> None:
        """Конструктор для инициализации подключения к API вакансий (api_name_service = vacancies)."""
        super().__init__("vacancies")

    def get_vacancies(self, employer_ids: List[str]) -> List[Dict[str, Any]]:
        """Метод для выполнения GET-запроса поиска вакансий.
        :param employer_ids: Список ID работодателей.
        :return: Список всех вакансий по запрашиваемым работодателям."""
        vacancies = []  # Итоговый список, в который складываются найденные вакансии.
        params: Dict[str, int | str] = {"employer_id": employer_ids, "page": 0, "per_page": 100}

        # Запрашиваем первую страницу, чтобы узнать количество доступных страниц
        data = self._make_request(params)
        # Получаем общее количество страниц (если нет, ставлю 1).
        # int() тут нужен, чтоб mypy точно определял, что total_pages это int и не выдавал ошибку при проверке
        total_pages = int(data.get("pages", 1))
        # Это лучше, чем 'while params["page"] != 20', так как предусмотрено исключение ВОЗМОЖНОГО бесконечного цикла
        while int(params["page"]) < total_pages:
            data = self._make_request(params)
            if not data.get("items"):  # Если вакансий нет, выходим из цикла
                break
            vacancies.extend(data["items"])  # Добавляем вакансии в итоговый список
            params["page"] = int(params["page"]) + 1  # Переходим на следующую страницу
        return vacancies
