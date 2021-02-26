from flask import flask

app = Flask (__name__)

@app.route("/")
def hello():
    return'alo mundo ! aqui e o mailsson '
if __name__"__main":
    app.run()