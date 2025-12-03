import base64
import hashlib
import requests
import os

WEBHOOK = os.environ["WEBHOOK"]

def send_image():
    with open("image.jpg", "rb") as f:
        img = f.read()

    base64_data = base64.b64encode(img).decode()
    md5 = hashlib.md5(img).hexdigest()

    data = {
        "msgtype": "image",
        "image": {
            "base64": base64_data,
            "md5": md5
        }
    }

    r = requests.post(WEBHOOK, json=data)
    print("发送结果：", r.text)

send_image()
