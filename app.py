from flask import Flask, render_template
from datetime import datetime

app = Flask("hello")

posts = [
    {
        "title": "O meu Primeiro Post",
        "body": "Aqui é o texto do Post",
        "author": "Renato",
        "created": datetime(2022,7,25)
    },
    {
        "title": "O meu Segundo Post",
        "body": "Aqui é o texto do Post",
        "author": "Renato2",
        "created": datetime(2022,7,26)
    },
]
@app.route("/")
def index():
    return render_template("index.html", posts=posts)

@app.route("/login")
def login():
    return render_template(login.html)
