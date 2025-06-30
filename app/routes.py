from flask import Blueprint, render_template
from .models import Task

main = Blueprint('main', __name__)

@main.route('/')
def home():
    lista_de_tarefas = Task.query.all()
    return render_template('home.html', task=lista_de_tarefas)
