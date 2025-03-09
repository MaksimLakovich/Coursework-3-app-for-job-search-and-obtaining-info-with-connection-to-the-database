from pathlib import Path

# Определение пути к корневой директории проекта, это будет использоваться далее в определении необходимых путей
BASE_DIR = Path(__file__).resolve().parent

# Определение пути к директории где будут размещаться JSON-файлы с различными данными приложения (../data/)
DATA_DIR = BASE_DIR / "data"


# Чтобы автоматически создать необходимую директорию (../data/), если ее еще не существует, я использую
# эту функцию. Будем вызывать ее при работе с классами-наследниками VacancyJSONSaver(BaseFileWork) и
# EmployerJSONSaver(BaseFileWork) в "src/file/...", что логично на мой взгляд, так как конструкторы классов (__init__)
# инициализирует путь к JSON-файлам с вакансиями и работодателями для дальнейшего взаимодействия.
def initialize_directories() -> None:
    """Функция создает необходимые директории и файлы, если они еще не существуют."""

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if not file_with_vacancies.exists():
        file_with_vacancies.write_text("[]", encoding="utf-8")

    if not file_with_employers.exists():
        file_with_employers.write_text("[]", encoding="utf-8")


# Определение пути к JSON-файлу с вакансиями, который размещается в проекте в директории (../data/)
file_with_vacancies = DATA_DIR / "json_data_vacancies.json"


# Определение пути к JSON-файлу с работодателями, который размещается в проекте в директории (../data/)
file_with_employers = DATA_DIR / "json_data_employers.json"


# Определение пути к JSON-файлу с пользовательскими настройками, который размещается в проекте в директории (../data/)
path_to_user_employer_settings = DATA_DIR / "user_employer_settings.json"
