from abc import ABC, abstractmethod


class BaseDBManager(ABC):
    """Абстрактный класс для пользовательского взаимодействия с базой данных."""

    @abstractmethod
    def __init__(self, database_name: str, params: dict) -> None:
        """Конструктор для подключения к БД.
        :param database_name: Название БД.
        :param params: Параметры подключения к БД."""
        pass

    @abstractmethod
    def get_companies_and_vacancies_count(self) -> list[tuple]:
        """Абстрактный метод для получения списка всех компаний и количества вакансий у каждой компании."""
        pass

    @abstractmethod
    def get_all_vacancies(self) -> list[tuple]:
        """Абстрактный метод для получения списка всех вакансий с указанием названия компании, названия вакансии,
         зарплаты и ссылки на вакансию."""
        pass

    @abstractmethod
    def get_avg_salary(self) ->  list[tuple]:
        """Абстрактный метод для получения средней зарплаты по вакансиям."""
        pass

    @abstractmethod
    def get_vacancies_with_higher_salary(self) -> list[tuple]:
        """Абстрактный метод для получения списка всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        pass

    @abstractmethod
    def get_vacancies_with_keyword(self, keyword: str) -> list[tuple]:
        """Абстрактный метод для получения списка всех вакансий, в названии которых есть переданные в метод слова.
        :param keyword: Ключевое слово для поиска."""
        pass

    def close_connection(self) -> None:
        """Абстрактный метод для закрытия соединения с БД."""
        pass
