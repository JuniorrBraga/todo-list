from flask import Blueprint, render_template, request, redirect, url_for
from .models import Task
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    lista_de_tarefas = Task.query.all()
    return render_template('home.html', tasks=lista_de_tarefas)

@main.route('/add', methods=['POST'])
def add_task():
    text_form = request.form['content']
    nova_tarefa = Task(content=text_form)
    db.session.add(nova_tarefa)
    db.session.commit()
    return redirect(url_for('main.home'))
    
