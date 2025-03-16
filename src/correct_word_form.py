def correct_word_form(count: int) -> str:
    """Функция подбирает правильное окончание для слова 'вакансия' в зависимости от кол-ва вакансий.
    :param count: Количество вакансий.
    :return: Слово 'вакансия' с корректным окончанием."""
    if count % 10 == 1 and count % 100 != 11:
        return "вакансия"
    elif 2 <= count % 10 <= 4 and (count % 100 < 10 or count % 100 >= 20):
        return "вакансии"
    else:
        return "вакансий"
