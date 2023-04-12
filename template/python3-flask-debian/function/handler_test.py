from handler import handle
import requests   
import json,io
from PIL import Image
import urllib.request

# Load the input image
with open('/Users/livion/Desktop/网站图片/apple-touch-icon.jpeg', 'rb') as f:
    img_data = f.read()

# Convert the image to hex format
hex_img = img_data.hex()

# Construct the input JSON payload
input_data = {'image': hex_img}
# Test your handler here
send_data = json.dumps(input_data)
# To disable testing, you can set the build_arg `TEST_ENABLED=false` on the CLI or in your stack.yml
# https://docs.openfaas.com/reference/yaml/#function-build-args-build-args

def test_handle():
    body = json.loads(send_data)
    ret = handle(body)
    return ret

ret = test_handle()
print(ret)
