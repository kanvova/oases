from flask import Flask, request, send_from_directory
from controllers.mainpage import mainpage
app = Flask(__name__, template_folder = "views")

@app.route('/')
def main():
    return mainpage.index()
