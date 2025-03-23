import os
from configparser import ConfigParser
from pathlib import Path

# Определение пути к корневой директории проекта, это будет использоваться далее в определении необходимых путей
BASE_DIR = Path(__file__).resolve().parent

# Определение пути к директории где будут размещаться JSON-файлы с различными данными приложения (../data/)
DATA_DIR = BASE_DIR / "data"


# Парсер для получения параметров подключения к БД, которые записаны в специальном файле database.ini
# Это необходимо для выполнения условия по использованию средств скрытия данных для доступа к БД.
def config(filename=None, section="postgresql"):
    """Функция для получения параметров подключения к БД."""
    # Определяем абсолютный путь к database.ini (предполагаем, что config.py тоже в корне проекта)
    if filename is None:
        filename = os.path.join(os.path.dirname(__file__), "database.ini")
    parser = ConfigParser()  # Создаю парсер
    parser.read(filename)  # Читаю конфигурационный файл
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            "Section {0} is not found in the {1} file.".format(section, filename)
        )
    return db


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
