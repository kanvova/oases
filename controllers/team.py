from flask import render_template
from models.modelTeam import modelTeam

class TeamController():
    def index(self):
        content = render_template("team/team.html", **modelTeam.getData())
        return content




teampage = TeamController()
