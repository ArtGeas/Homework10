from flask import Flask
from utils import format_candidates
from utils import get_all
from utils import get_by_pk
from utils import get_by_skill

app = Flask(__name__)


@app.route('/')
def page_main():
    """Главная страница"""
    candidates = get_all()
    result = format_candidates(candidates)
    return result


@app.route('/candidate/<int:uid>')
def page_candidate(uid):
    """Страница кандидата"""
    candidate = get_by_pk(uid)
    result = f'<img src="{candidate["picture"]}">'
    result += format_candidates([candidate])
    return result


@app.route('/skills/<skill>')
def page_skills(skill):
    """Страница кандидатов с навыком"""
    skill_lower = skill.lower()
    candidates = get_by_skill(skill_lower)
    result = format_candidates(candidates)
    return result


app.run()
