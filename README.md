# Проект 3. Приложение для получения данных о компаниях и вакансиях с сайта hh.ru и их загрузки в спроектированные таблицы в БД PostgreSQL

[1. Цель и суть проекта](#title1) / 
[2. Основные модули](#title2) / 
[3. Вспомогательные модули](#title3) / 
[4. Функция взаимодействия с пользователем](#title4) / 
[5. Установка проекта](#title5) / 




## <a id="title1">1. Цель и суть проекта</a>

Реализовать программу, которая с помощью API будет получать информацию о компаниях и вакансиях с платформы HeadHunter (возможно использовать с другими аналогичными ресурсами по поиску работы), загружать и сохранять результаты поиска в в спроектированные таблицы в БД PostgreSQL и позволять удобно работать с ними (пользовательские запросы на получение отфильтрованных данных).

### Функциональный код разбит на модули:
1. `Получение данных с API`
   - Получение данных о работодателях и их вакансиях с сайта *hh.ru*. Для этого используется публичный API hh.ru и библиотека *requests*.
   - Выбор не менее 10 компаний, от которых будут загружаться данные о вакансиях по API.
2. `Создание базы данных PostgreSQL и её структурирование`
   - Спроектированы таблицы в БД *PostgreSQL* для хранения полученных данных о работодателях и их вакансиях. Для работы с БД используется библиотека *psycopg2*.
3. `Загрузка данных в БД`
   - Реализован код, который заполняет созданные в БД PostgreSQL таблицы данными о работодателях и их вакансиях.
4. `Разработка класса DBManager для работы с данными`
   - Создан ***class DBManager*** для работы с данными в БД.
5. `Создание интерфейса для взаимодействия с пользователем`
   - "точка входа" - модуль, запустив который можно получить результат всех реализованных в проекте функциональностей.
6. `Модуль со вспомогательными функциями`

### Документация для сбора вакансий с hh.ru:
  - Ссылка на API: https://github.com/hhru/api/.

### Выходные данные:
   - Отфильтрованные и отсортированные вакансии, выводимые пользователю через консоль.



  
## <a id="title2">2. Основные модули / функции</a>

### Абстрактные классы:
### Базовые классы:




## <a id="title3">3. Вспомогательные модули / функции</a>




## <a id="title4">4. Взаимодействие пользователя с программой (модуль *main.py*)</a>

Модуль ***main.py*** содержит код для ...




## <a id="title5">5. Установка проекта</a>
1. Клонируйте репозиторий:
```
git clone https://github.com/MaksimLakovich/Coursework-3-app-for-job-search-and-obtaining-info-with-connection-to-the-database.git
```
2. Установите зависимости:
```
poetry install
```
