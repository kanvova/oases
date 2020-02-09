import json
from flask import render_template, session, request, redirect, url_for

class AuthController():
    def index(self, action):
        if action == 'login':
            return AuthController.login()
        if action == 'logout':
            return AuthController.logout()

        if session.get("admin") is None:
            return render_template("auth/form.html");
        else:
            return redirect(url_for('main'))

    def login():
        config  = {
            "login" : "login",
            "password" : "password"
        }

        login = request.form['login']
        password = request.form['password']

        if login == config["login"] and password == config["password"]:

            session['admin'] = 1
            return json.dumps({
                "status": "success"
            })

        return json.dumps({
            "status": "error"
        })

    def logout():
        session.clear()
        return json.dumps({
            "status": "success"
        })

authcontroller = AuthController()
