import requests   
import json,io
from PIL import Image

# Load the input image
with open('/Users/livion/Desktop/网站图片/icon.jpeg', 'rb') as f:
    img_data = f.read()


# Set the function endpoint URL
endpoint_url = 'http://10.1.81.24:31112/function/debug'

# Send the HTTP POST request
response = requests.post(endpoint_url, files={'file': img_data},timeout=30)
 
# Process the response
if response.ok:
    print("OK")
else:
    print(f"Error: {response.content}")

