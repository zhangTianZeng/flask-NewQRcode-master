#coding:utf-8
from flask import Flask
from zxing.jiexi import jieXi
from generate.shengcheng import shengCheng
app = Flask(__name__)

app.register_blueprint(shengCheng)
app.register_blueprint(jieXi)


@app.route("/")
def index():
    return "ok"


if __name__=="__main__":
    app.run(debug=True,host='127.0.0.1',port=8000)