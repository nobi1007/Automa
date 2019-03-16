import json
import requests
import cv2

img = cv2.imread('clouds.jpg',1)
cv2.imwrite('clouds1.jpg',img)

headers = {"Authorization": "Bearer ya29.GlvPBn766KGX0G55W2xXCin9FNUP_JVDnpxFxTMM_ZcTSyJN6XkpkgG86vTnpbvit-9We9DlIPuqFdLF8a1ruwYl5YHmR6164VtmIX-gt1wPvv1YPEeaejtnHpY5"}
para = {
    "name": "clouds.jpg",
    "parents": ["19fhPFZmvcjPt6QVfd7Fjs6lbDxBHKKwk"]
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
