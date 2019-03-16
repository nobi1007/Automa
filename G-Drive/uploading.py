import json
import requests
import cv2

img = cv2.imread('name of the downloaded image',0)
cv2.imwrite('name of the image after editing',img)

headers = {"Authorization": "Bearer (Your Auth Key without braces)"}
para = {
    "name": "name to be displayed for the uploaded image",
    "parents": ["id of the g-drive folder from where the file has to be downloaded"]
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': ('image/jpg',open("./name of the edited file", "rb"))
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)

print(r.text)
