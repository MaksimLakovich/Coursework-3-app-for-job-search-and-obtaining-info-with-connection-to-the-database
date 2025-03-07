from pathlib import Path

# Определение пути к корневой директории проекта, это будет использоваться далее в определении необходимых путей
BASE_DIR = Path(__file__).resolve().parent

# Определение пути к директории где будут размещаться JSON-файлы с различными данными приложения (../data/)
DATA_DIR = BASE_DIR / "data"

# Определение пути к JSON-файлу с пользовательскими настройками, который размещается в проекте в директории (../data/)
path_to_user_employer_settings = DATA_DIR / "user_employer_settings.json"
