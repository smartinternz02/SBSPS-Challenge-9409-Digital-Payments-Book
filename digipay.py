from flask import Flask

app = Flask(__name__)

@app.route("/")
def digipay():
    return "<h1>Hello, Users!</h1> <hr> <p>Hi Everyone, Welcome to your Digital Payments history</p>"