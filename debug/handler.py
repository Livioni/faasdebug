import json,io,datetime
from minio import Minio
from PIL import Image

client = None

def init_client():
    global client
    client = Minio(
    # "10.1.81.24:9000", #minio数据库的API地址
    "192.168.31.142:9000", 
    access_key="minioadmin", #RootUser
    secret_key="minioadmin", #RootPassword
    secure=False, #必须加上这一项，否则会按照Amazon S3 Compatible Cloud Storage来处理
)

def handle(image_bytes):
    try:
        if client is None:
            init_client()
        image = Image.open(io.BytesIO(image_bytes))
        buffer = io.BytesIO()
        my_image = image.convert('RGB')
        my_image.save(buffer, format="JPEG")
        buffer.seek(0) #重置指针 非常重要
        image_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        client.put_object("mybucket", image_name, buffer, len(buffer.getvalue()),content_type="image/jpg")
        response_body = {
            "message": "success",
            "image_name": image_name
        }
        return json.dumps(response_body)
    except Exception as e:
        return str(e)
