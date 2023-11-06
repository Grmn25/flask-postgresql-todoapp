import os
from flask import Flask


def create_app():
    app = Flask(__name__, static_url_path='/static',
                )

    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE=os.environ.get('FLASK_DATABASE'),
    )

    from . import db
    from . import auth
    from . import todo

    db.init_app(app)

    app.register_blueprint(auth.bp)
    app.register_blueprint(todo.bp)

    return app
