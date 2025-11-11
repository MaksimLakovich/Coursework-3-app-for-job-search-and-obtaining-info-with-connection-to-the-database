import json
from pathlib import Path
from typing import Any, Dict, List, Union


def read_json_data_vacancies(path_to_file: Union[str, Path]) -> List[Dict[str, Any]]:
    """1) Функция читает данные о вакансиях из json-файла. 2) Если json-файла нет, то возвращается пустой список.
    :param path_to_file: Путь к json-файлу.
    :return: Данные о вакансиях."""

    try:
        with open(path_to_file) as json_data:
            vacancies_data: List[Dict[str, Any]] = json.load(json_data)
            return vacancies_data

    except FileNotFoundError as e:
        print(f"❌ Файл с json-данными не найден: {path_to_file}. {e}")
    except json.JSONDecodeError:
        print(f"❌ Ошибка декодирования JSON в файле: {path_to_file}")

    return []
