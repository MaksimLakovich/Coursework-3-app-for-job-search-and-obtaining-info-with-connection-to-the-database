from src.objects.employer import Employer


def employer_to_dict(employer: Employer) -> dict:
    """Функция для преобразования объекта Employer в словарь."""
    return {slot: getattr(employer, slot) for slot in Employer.__slots__}
