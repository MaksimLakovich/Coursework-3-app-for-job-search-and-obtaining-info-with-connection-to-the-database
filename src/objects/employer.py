from typing import Any


class Employer:
    """Класс для работы с объектом 'работодатель'."""

    __slots__ = ["employer_id", "employer_name", "employer_url"]

    def __init__(self, employer_id: str, employer_name: str, employer_url: str):
        """Конструктор для создания работодателя. Инициализация экземпляра класса (объекта)."""
        self.employer_id = employer_id
        self.employer_name = employer_name
        self.employer_url = employer_url

    def __str__(self) -> str:
        """Магический метод возвращает строковое представление работодателя для print()."""
        return (f"{self.employer_name} ({self.employer_url})")

    def __repr__(self) -> str:
        """Магический метод возвращает краткую строку для отладки (repr)."""
        return f"Employer({self.employer_id}, {self.employer_name})"

    @staticmethod
    def cast_to_object_list(vacancies_data: list[dict[str, Any]]) -> list["Employer"]:
        """Статик-метод преобразует список словарей в список объектов Employer.
        :param vacancies_data: Файл с полученными вакансиями, которые сформировались в запросе API сервиса вакансий.
        :return: Возвращает список объектов Employer."""
        return [
            Employer(
                employer_id=data["employer"]["id"],
                employer_name=data["employer"]["name"],
                employer_url=data["employer"]["url"],
            )
            for data in vacancies_data
        ]
