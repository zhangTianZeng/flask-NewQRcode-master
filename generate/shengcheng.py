#coding:utf-8
from flask import Blueprint,render_template, request,json
from generate import generate_image
shengCheng = Blueprint("shengCheng",__name__)

@shengCheng.route("/")
def index():
    return render_template("index.html")

#生成的界面
@shengCheng.route("/shengCheng/")
def shengcheng():
    return render_template("shengcheng.html")

#生成的图片的接口
@shengCheng.route("/shengcheng_image/",methods={'post'})
def shengcheng_image():
    strr = request.values.get('message')
    print strr
    url  = generate_image(strr)
    return json.dumps({"code": 0,
                       "images":url,})

