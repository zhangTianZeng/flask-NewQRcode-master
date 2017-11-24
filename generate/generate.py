#coding:utf-8
import qrcode,uuid,os
from qiniusdk import qiniu_upload_file

save_dir = 'D:/upload/'
def generate_image(strr):
    img = qrcode.make(strr)  # QRCode信息
    file_name = str(uuid.uuid1()).replace("-","")+".jpg"
    path = os.path.join(save_dir,file_name)
    print path
    img.save(path)
    url = qiniu_upload_file(file_name)
    return url

