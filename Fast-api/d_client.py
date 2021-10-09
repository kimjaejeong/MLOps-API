import json
import requests
import numpy as np
from PIL import Image

image = Image.open('test_image.jpg')
pixels = np.array(image)

headers = {'Content-Type':'application/json'}
address = 'http://ip주소/predict'
data = {'images':pixels.tolist()}

payload = {
    'data' : json.dumps(data)
}

result = requests.post(address, data=json.dumps(data), headers=headers)
print(str(result.content, encoding='utf-8'))