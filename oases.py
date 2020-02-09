from flask import Flask, session, request, render_template, redirect, url_for
from flask_babel import Babel, _
from controllers.mainpage import mainpage
from controllers.team import teampage
from controllers.publications import publicationspage
from controllers.auth import authcontroller

import secrets

app = Flask(__name__, template_folder = "views")
app.config["SECRET_KEY"] = secrets.token_urlsafe(16)
app.config.from_pyfile('config.py')

babel = Babel(app)


@app.route('/')
def main():
    return mainpage.index()

@app.route('/about')
def about():
    return render_template("about/about.html")

@app.route('/team')
def team():
    return teampage.index()

@app.route('/publications')
def publicationslist():
    return publicationspage.index('list')
@app.route('/publications/<id>', methods=['GET', 'POST'])
def publications(id):
    return publicationspage.index(id)

@app.route('/project')
def project():
    return render_template("project/project.html")

@app.route('/auth/<action>', methods=['GET', 'POST'])
def auth(action):
    return authcontroller.index(action)

@app.route('/language/<language>')
def set_language(language=None):
    session['language'] = language
    return redirect(url_for('main'))


@babel.localeselector
def get_locale():
    if not session.get("language") is None:
        return session.get("language")
    return request.accept_languages.best_match(app.config['LANGUAGES'])
