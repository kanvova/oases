from flask import Flask
from controllers.mainpage import mainpage
app = Flask(__name__, template_folder = "views")

@app.route('/')
def main():
    return mainpage.index()
