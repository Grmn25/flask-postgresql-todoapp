from flask import (Blueprint, flash, g, redirect,
                   render_template, url_for, request)
from werkzeug.exceptions import abort
from app.db import get_db
from app.auth import login_required

bp = Blueprint('todo', __name__)


@bp.route('/')
@login_required
def index():
    db, c = get_db()
    c.execute(
        "SELECT t.todo_id, t.description, u.username, t.completed, t.created_at FROM todo t JOIN usuario u ON created_by= u.usuario_id WHERE t.created_by=%s ORDER BY created_at DESC", (
            g.user[0],)
    )
    tareas = c.fetchall()
    return render_template('todo/index.html', tareas=tareas)


@bp.route('/crear', methods=['GET', 'POST'])
@login_required
def crear():
    if request.method == 'POST':
        description = request.form['description']
        error = None

        if not description:
            error = 'Description is required.'

        if error is not None:
            flash(error)
        else:
            db, c = get_db()
            c.execute(
                "INSERT INTO todo (description, completed, created_by) VALUES (%s, %s, %s)", (
                    description, False, g.user[0])
            )
            db.commit()
            return redirect(url_for("todo.index"))

    return render_template('todo/crear.html')


def get_todo(id):
    db, c = get_db()
    c.execute(
        'SELECT t.todo_id, t.description, t.completed, t.created_by, t.created_at, u.username '
        'FROM todo t JOIN usuario u ON t.created_by=u.usuario_id WHERE t.todo_id=%s', (
            id,)
    )

    todo = c.fetchone()
    if todo is None:
        abort(404, "The todo with id {0} not exist".format(id))

    return todo


@bp.route('/<int:id>/actualizar', methods=['GET', 'POST'])
@login_required
def actualizar(id):
    todo = get_todo(id)
    if request.method == 'POST':
        description = request.form['description']
        completed = True if request.form.get('completed') == 'on' else False
        error = None
        if not description:
            error = "Description is required"
        if error is not None:
            flash(error)
        else:
            db, c = get_db()
            c.execute(
                "UPDATE todo SET description= %s, completed =%s"
                " WHERE todo_id=%s AND created_by=%s", (
                    description, completed, id, g.user[0])
            )
            db.commit()
            return redirect(url_for('todo.index'))
    return render_template('todo/actualizar.html', todo=todo)


@bp.route('/<int:id>/eliminar', methods=['GET', 'POST'])
@login_required
def eliminar(id):
    db, c = get_db()
    c.execute(
        "DELETE FROM todo WHERE todo_id=%s AND created_by=%s", (id, g.user[0])
    )
    db.commit()
    return redirect(url_for('todo.index'))
