import json
import requests
import cv2

img = cv2.imread('clouds.jpg',1)
cv2.imwrite('clouds1.jpg',img)

headers = {"Authorization": "Bearer (Your Auth Key without braces)"}
para = {
    "name": "clouds.jpg",
    "parents": ["id of the g-drive folder from where the file has to be downloaded"]
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': ('image/jpg',open("./clouds1.jpg", "rb"))
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)

print(r.text)
