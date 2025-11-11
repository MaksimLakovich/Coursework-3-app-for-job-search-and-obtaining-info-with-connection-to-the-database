from typing import Any

from src.exchange_rates import get_exchange_rates


class Vacancy:
    """Класс для работы с объектом 'вакансия'."""

    __slots__ = [
        "employer_id",
        "employer_name",
        "employer_url",
        "vacancy_id",
        "name",
        "area_name",
        "alternate_url",
        "salary_from",
        "salary_to",
        "salary_currency",
        "published_at",
        "archived",
        "snippet_responsibility",
    ]

    def __init__(
        self,
        employer_id: str,
        employer_name: str,
        employer_url: str,
        vacancy_id: str,
        name: str,
        area_name: str,
        alternate_url: str,
        salary_from: float | None,
        salary_to: float | None,
        salary_currency: str | None,
        published_at: str,
        archived: bool,
        snippet_responsibility: str,
    ):
        """Конструктор для создания вакансии. Инициализация экземпляра класса (объекта)."""
        self.employer_id = employer_id
        self.employer_name = employer_name
        self.employer_url = employer_url
        self.vacancy_id = vacancy_id
        self.name = name
        self.area_name = area_name
        self.alternate_url = alternate_url
        self.salary_from = self.__validate_salary(salary=salary_from, currency=salary_currency)
        self.salary_to = self.__validate_salary(salary=salary_to, currency=salary_currency)
        self.salary_currency = self.__validate_currency(salary_currency)
        self.published_at = published_at
        self.archived = archived
        self.snippet_responsibility = snippet_responsibility or ""

    def __str__(self) -> str:
        """Магический метод возвращает строковое представление вакансии для print()."""
        return (
            f"📌 {self.name} ({self.area_name})\n"
            f"💰 Зарплата: {self.salary_from} - {self.salary_to} {self.salary_currency}\n"
            f"🔗 {self.alternate_url}\n"
            f"📅 Опубликовано: {self.published_at}\n"
            f"📝 Описание: {self.snippet_responsibility[:1000]}..."
        )  # Обрезаю слишком длинное описание до 1000.

    def __repr__(self) -> str:
        """Магический метод возвращает краткую строку для отладки (repr)."""
        return f"Vacancy({self.vacancy_id}, {self.name}, {self.salary_from}-{self.salary_to} {self.salary_currency})"

    def __validate_currency(self, currency: str | None) -> str:
        """Приватный метод валидации валюты зарплаты.
        :param currency: Значение валюты, которое поступает из запроса к API сервиса вакансий.
        :return: Возвращает строку 'RUB', если:
            1) Если валюта не указана, то указываем по умолчанию RUB;
            2) Если была конвертация (валюта ≠ RUB), то также заменяем её на RUB."""
        if currency is None or currency != "RUB":
            return "RUB"
        return currency

    def __validate_salary(self, salary: float | None, currency: str | None) -> float:
        """Приватный метод проверки значения зарплаты (валидация пустых значений), а также выполнения конвертации
        валюты в RUB если валюта в вакансии != RUB.
        :param salary: Значения 'from' и 'to' из 'salary', которые поступают из запроса к API сервиса вакансий.
        :param currency: Значение валюты, которое поступает из запроса к API сервиса вакансий.
        :return: Возвращает дробное число:
                1) ноль, если зарплата не указана на сервисе вакансий;
                2) конвертируемое значение по текущему курсу валют, если зарплата в отличной от RUB валюте.
                3) текущее значение без изменения, если зарплата на сервисе вакансий указана в RUB."""
        if not salary or salary <= 0:
            return 0.0
        if currency and currency != "RUR":
            return salary * get_exchange_rates(currency_name=currency)
        # Возвращаем исходное значение зарплаты, так как оно в RUB и не требует конвертации
        return salary

    @staticmethod
    def cast_to_object_list(vacancies_data: list[dict[str, Any]]) -> list["Vacancy"]:
        """Статик-метод преобразует список словарей в список объектов Vacancy.
        :param vacancies_data: Файл с полученными вакансиями, которые сформировались в запросе API сервиса вакансий.
        :return: Возвращает список объектов Vacancy."""
        return [
            Vacancy(
                employer_id=data["employer"]["id"],
                employer_name=data["employer"]["name"],
                employer_url=data["employer"]["alternate_url"],
                vacancy_id=data["id"],
                name=data["name"],
                area_name=data["area"]["name"],
                alternate_url=data["alternate_url"],
                # Проверяю наличие salary. Указываю None, если salary отсутствует
                salary_from=(data.get("salary") or {}).get("from"),
                # Проверяю наличие salary. Указываю None, если salary отсутствует
                salary_to=(data.get("salary") or {}).get("to"),
                # Проверяю наличие salary. Указываю None, если salary отсутствует
                salary_currency=(data.get("salary") or {}).get("currency"),
                published_at=data["published_at"],
                archived=data["archived"],
                snippet_responsibility=data["snippet"].get("responsibility", ""),
            )
            for data in vacancies_data
        ]
