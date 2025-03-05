from src.hh_api import HeadHunterAPI


def user_interaction() -> None:
    """Функция для взаимодействия пользователя с программой."""

    platforms = ["HeadHunter"]  # Сейчас это будет только "HeadHunter", но в будущем можно расширить другими сервисами

    while True:
        select_platform = input(f"Выберите платформу для поиска вакансий ({', '.join(platforms)}): ").strip()
        if select_platform in platforms:
            print(f"✅ Выбрана платформа: {select_platform}")
            break
        else:
            print(f"❌ Ошибка: Платформа '{select_platform}' не поддерживается. Введите платформу из списка.")

    # ШАГ 1: Подключение к HeadHunter и получение вакансии по .......списку работодателей (тут 3 фишки).......
    if select_platform == "HeadHunter":
        # search_query = input("Введите вариант запроса .....(тут 3 фишки).....: ").strip()
        # search_employers_list = "78638"
        search_employers_list = ["1455", "78638"]
        hh_api = HeadHunterAPI()  # Создание экземпляра класса для работы с API HeadHunter
        hh_data = hh_api.load_vacancies(search_employers_list)  # Получение вакансий по работодателям из списка
        print(hh_data)


if __name__ == "__main__":
    user_interaction()
