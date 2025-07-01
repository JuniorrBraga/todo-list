from flask import Blueprint, render_template, request, redirect, url_for
from .models import Task
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    lista_de_tarefas = Task.query.order_by(Task.date_created).all()
    return render_template('home.html', tasks=lista_de_tarefas)

@main.route('/add', methods=['POST'])
def add_task():
    text_form = request.form['content']
    nova_tarefa = Task(content=text_form)
    db.session.add(nova_tarefa)
    db.session.commit()
    return redirect(url_for('main.home'))

@main.route('/update/<int:task_id>', methods=['POST'])
def update(task_id):
    task_att = Task.query.get_or_404(task_id)
    task_att.completed = not task_att.completed
    db.session.commit()
    return redirect(url_for('main.home'))

@main.route('/delete/<int:task_id>')
def delete(task_id):
    task_delete = Task.query.get_or_404(task_id)
    db.session.delete(task_delete)
    db.session.commit()
    return redirect(url_for('main.home'))