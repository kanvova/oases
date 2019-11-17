from flask import render_template
from models.modelMainpage import modelMainpage

class MainpageController():
    def index(self):
        content = render_template("tpl/header.html")
        content += render_template("mainpage/mainpage.html", **modelMainpage.getData())
        content += render_template("tpl/footer.html")
        return content




mainpage = MainpageController()
