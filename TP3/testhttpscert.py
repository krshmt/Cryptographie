# server.py
from flask import Flask

SECRET_MESSAGE = "gneugneu je m'appelle louis et ca ne fonctionne pas"
app = Flask(__name__)

@app.route("/")
def get_secret_message():
    return SECRET_MESSAGE


if __name__ == "__main__":
    app.run()