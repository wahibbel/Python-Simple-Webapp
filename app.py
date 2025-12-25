import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Hey Guys!"

@app.route('/lets go')
def hello():
    return 'nope i am not ready'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)