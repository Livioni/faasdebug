import requests   
import json,io
from PIL import Image

# Load the input image
with open('/Users/livion/Desktop/网站图片/icon.jpeg', 'rb') as f:
    img_data = f.read()

# Convert the image to hex format
hex_img = img_data.hex()

# Construct the input JSON payload
input_data = {'image': hex_img}

# Set the function endpoint URL
endpoint_url = 'http://10.1.81.24:31112/function/debug'

send_data = json.dumps(input_data)

# Send the HTTP POST request
response = requests.post(endpoint_url, data=send_data,timeout=30)

# Process the response
if response.ok:
    print("OK")
else:
    print(f"Error: {response.content}")

