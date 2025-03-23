import json
from pathlib import Path
from typing import Any, Dict, Union


def read_json_user_employer_settings(path_to_file: Union[str, Path]) -> Dict[str, Any]:
    """1) Функция считывает из json-файла заданный по умолчанию пользовательский перечень работодателей (10 компаний)
    для дальнейшего поиска и сбора всех вакансий по указанным в файле компаниям. 2) Если пользовательских настроек нет,
    то возвращается пустой список, который потом, с помощью функции пользовательского взаимодействия user_interaction()
    в main.py, будет заполняться/наполняться самим пользователем.
    :param path_to_file: Путь к json-файлу.
    :return: Перечень названий работодателей в формате dict."""

    try:
        with open(path_to_file) as json_data:
            employer_names: Dict[str, Any] = json.load(json_data)
            return employer_names

    except FileNotFoundError as e:
        print(f"❌ Файл с json-данными не найден: {path_to_file}. {e}")
    except json.JSONDecodeError:
        print(f"❌ Ошибка декодирования JSON в файле: {path_to_file}")

    return {}
