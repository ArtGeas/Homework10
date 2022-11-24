import json


def load_candidates():
    """Загружает данные json"""
    with open("candidates.json", "r", encoding='utf-8') as file:
        candidates = json.load(file)
    return candidates


def format_candidates(candidates):
    """Форматирование списка кандидатов"""

    result = '<pre>'
    for candidate in candidates:
        result += f"""
               {candidate["name"]}
               {candidate["position"]}
               {candidate["skills"]}
           """
    result += "</pre>"
    return result


def get_all():
    return load_candidates()


def get_by_pk(pk):
    candidates = get_all()
    for candidate in candidates:
        if candidate['pk'] == pk:
            return candidate
    return None

def get_by_skill(skill_name):
    candidates = get_all()
    result = []
    for candidate in candidates:
        if skill_name in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result
