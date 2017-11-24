#coding:utf-8

from qiniu import Auth,put_file
import os

#需要填写你的 Access Key 和 Secret Key
access_key = 'hOAlP_XtJ1cRpLHTJJOZHbZQ-TiAbTXvATkYaViK'
secret_key = 'l_Ml3DDoRsPEZl7bYH4uyu0A4sv5u8xGSSvEn6NJ'
#构建鉴权对象
q = Auth(access_key,secret_key)
#要上传的空间
bucket_name = 'shareimage'
domain_prefix = 'http://oxzuxtk23.bkt.clouddn.com'
save_dir = 'D:/upload/'

def qiniu_upload_file(save_file_name):
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, save_file_name)

    ret, info = put_file(token ,save_file_name,os.path.join(save_dir,save_file_name))
    #ret,info = put_stream(token,save_file_name,source_file.save,"qiniu",source_file.stream.tell())

    if info.status_code == 200:


        return domain_prefix +"/"+ save_file_name
    return None

