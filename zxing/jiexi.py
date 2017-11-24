#coding:utf-8
from flask import Blueprint,render_template, request,json
import uuid,os
from qiniusdk import qiniu_upload_file
from tests import *
save_dir = 'D:/upload/'
jieXi = Blueprint("jieXi",__name__)

@jieXi.route("/jieXi/")
def jiexi():
    return render_template("jiexi.html")

#生成的图片的接口
@jieXi.route("/getImage/",methods={'post'})
def getImage():
    file = request.files['file']
    print(file.filename)
    if file!=None:
        file_ext = ''
        if file.filename.find('.') > 0:
            file_ext = file.filename.rsplit('.', 1)[1].strip().lower()
            file_name = str(uuid.uuid1()).replace("-", "") +"."+ file_ext
            path = os.path.join(save_dir, file_name)
            file.save(path)
            path = "file:///"+path
            print(path)

            action = Action(path)
            strr = action.test_codereader()

            print(strr)
            url = qiniu_upload_file(file_name)
            print(url)

            return json.dumps({"key_one":[{"code": 0},{"images":url},{"strr":strr}]})
    return json.dumps({"code": 1})
