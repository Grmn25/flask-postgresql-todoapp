import functools
from flask import (Blueprint, flash, render_template, redirect,
                   request, url_for, session, g)

from werkzeug.security import check_password_hash, generate_password_hash
from app.db import get_db

bp = Blueprint('auth', __name__, url_prefix="/auth")


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db, c = get_db()
        error = None
        c.execute(
            "SELECT usuario_id FROM usuario WHERE username = %s", (username,)
        )
        if not username:
            error = 'Username es requerido'

        if not password:
            error = 'Password es requerido'
        elif c.fetchone() is not None:
            error = 'Usuario {} se encuentra registrado.'.format(username)

        if error is None:
            c.execute(
                'INSERT INTO usuario (username, password) VALUES (%s, %s) RETURNING usuario_id',
                (username, generate_password_hash(password))
            )
            user = c.fetchone()
            db.commit()
            session.clear()
            session['user_id'] = user['usuario_id']
            return redirect(url_for('todo.index'))
        flash(error)
    return render_template('auth/registrar.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db, c = get_db()
        error = None
        c.execute(
            "SELECT * FROM usuario WHERE username = %s", (username,)
        )
        user = c.fetchone()

        if user is None:
            error = 'Username y/o contraseña incorrecta'
        elif not check_password_hash(user[2], password):
            error = 'Username y/o contraseña incorrecta'

        if error is None:
            session.clear()
            session['user_id'] = user['usuario_id']
            print('session')
            print(session['user_id'])
            print('user[0]')
            print(user[0])
            return redirect(url_for('todo.index'))
        flash(error)

    return render_template("auth/login.html")


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        db, c = get_db()
        c.execute('SELECT * FROM usuario WHERE usuario_id = %s', (user_id,))
        g.user = c.fetchone()


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
