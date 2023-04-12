import requests   
import json,io
from PIL import Image
import urllib.request

# Load the input image
with open('/Users/livion/Desktop/网站图片/icon.jpeg', 'rb') as f:
    img_data = f.read()

# Convert the image to hex format
hex_img = img_data.hex()

# Construct the input JSON payload
input_data = {'image': hex_img}

# Set the function endpoint URL
# endpoint_url = 'http://10.62.61.112:31112/function/keypoint'
# endpoint_url =  'http://gateway.openfaas.svc.cluster.local:8080/function/debug'
# endpoint_url = 'http://10.62.61.112:31112/function/debug'
# endpoint_url = 'http://127.0.0.1:5000' 
endpoint_url = 'http://10.1.81.24:31112/function/debug'

send_data = json.dumps(input_data)

# Send the HTTP POST request
response = requests.post(endpoint_url, data=send_data,timeout=30)#, headers={'Content-Type': 'application/octet-stream'})
# response = urllib.request.Request(url=endpoint_url, data=send_data, method='POST')
# Process the response
if response.ok:
    print("OK")
else:
    print(f"Error: {response.content}")

