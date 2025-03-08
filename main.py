from config import path_to_user_employer_settings
from src.api.hh_area_api import HeadHunterAreasAPI
from src.api.hh_employer_api import HeadHunterEmployersAPI
from src.api.hh_vacancy_api import HeadHunterVacanciesAPI
from src.get_employers_name import get_employer_names_for_search


def user_interaction(path_to_settings: str) -> None:
    """Функция для взаимодействия пользователя с программой."""

    employers = get_employer_names_for_search(path_to_settings)["employer_names"]
    area_name = ["Все города"]
    search_text = ["Не задано"]

    while True:
        print(f"\nТекущий список компаний: {employers}")
        print(f"Текущий список городов: {area_name}")
        print(f"Текущий список ключевых слов: {search_text}")
        print("\nУстановите дополнительные параметры поиска вакансий и работодателей:")
        print("1 - ЗАПУСТИТЬ ПОИСК ПО ЗАДАННЫМ ПАРАМЕТРАМ")
        print("2 - Изменить текущий список компаний в поиске")
        print("3 - Изменить список городов в поиске вакансий")
        print("4 - Изменить ключевые слова в поиске вакансий")
        print("5 - Сбросить дополнительные параметры и вернуться к настройкам по умолчанию")
        print("6 - Выход из программы")
        choice = input("Выберите действие (1-6): ").strip()

        if choice == "1":

            platforms = ["HeadHunter"]  # Сейчас это только "HeadHunter", но в будущем можно добавить другие сервисы

            while True:
                select_platform = input(f"\nВыберите платформу для поиска вакансий ({', '.join(platforms)}): ").strip()
                if select_platform in platforms:
                    print(f"✅ Выбрана платформа: {select_platform}")
                    break
                else:
                    print(f"❌ Ошибка: Платформа '{select_platform}' не поддерживается. Введите платформу из списка.")

            # ШАГ 1: Подключение к HeadHunter
            if select_platform == "HeadHunter":
                # Получаем список названий организаций (10 работодателей по умолчанию)
                search_employers_list = get_employer_names_for_search(path_to_settings)
                # Создаем экземпляр класса для работы с API работодателей и получаем список ID работодателей
                hh_employer_api = HeadHunterEmployersAPI()
                hh_list_employer_ids = hh_employer_api.get_employer_ids(search_employers_list["employer_names"])
                # Создаем экземпляр класса для работы с API регионов/городов и получаем список ID городов
                hh_area_api = HeadHunterAreasAPI()
                hh_list_area_ids = hh_area_api.get_area_ids(area_name)
                print(hh_list_area_ids)
                print(type(hh_list_area_ids))
                # Создаем экземпляр класса для работы с API вакансий и получаем все вакансии по данным работодателям
                hh_vacancy_api = HeadHunterVacanciesAPI()
                hh_list_vacancies = hh_vacancy_api.get_vacancies(hh_list_employer_ids, hh_list_area_ids)
                print(hh_list_vacancies)
                print(type(hh_list_vacancies))

        elif choice == "2":
            pass

        elif choice == "3":
            user_choice = input("Введите город (или набор городов через запятую): ").strip().title()
            if area_name[0] == "Все города":
                area_name = user_choice.split(",")
                print(type(area_name))
                print(area_name)
            else:
                area_name.extend(user_choice.split(","))
                print(type(area_name))
                print(area_name)

        elif choice == "4":
            pass

        elif choice == "5":
            employers = get_employer_names_for_search(path_to_settings)["employer_names"]
            area_name = ["Все города"]
            search_text = ["Не задано"]
            print("✅Дополнительные параметры сброшены и возвращены настройки по умолчанию.")

        elif choice == "6":
            print("✅Завершение работы.")
            break

        else:
            print("❌Ошибка: Некорректный ввод. Попробуйте снова.")


if __name__ == "__main__":
    user_interaction(path_to_user_employer_settings)
