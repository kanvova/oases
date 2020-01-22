from flask import render_template
from models.modelMainpage import modelMainpage

class MainpageController():
    def index(self):
        content = render_template("mainpage/mainpage.html", **modelMainpage.getData())
        return content




mainpage = MainpageController()
