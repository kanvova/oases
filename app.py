from flask import Flask, session, request, redirect, url_for
from flask_babel import Babel, _
from controllers.mainpage import mainpage

import secrets

app = Flask(__name__, template_folder = "views")
app.config["SECRET_KEY"] = secrets.token_urlsafe(16)
app.config.from_pyfile('config.py')

babel = Babel(app)

@app.route('/')
def main():
    return mainpage.index()

@app.route('/language/<language>')
def set_language(language=None):
    session['language'] = language
    return redirect(url_for('main'))


@babel.localeselector
def get_locale():
    if not session.get("language") is None:
        return session.get("language")
    return request.accept_languages.best_match(app.config['LANGUAGES'])
