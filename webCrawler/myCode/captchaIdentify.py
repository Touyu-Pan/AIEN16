import re

import pytesseract
from PIL import Image

# replace tesseract cmd path with your own path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = Image.open('base64-3.png').convert('L')
# adjust threshold to get best confidence
threshold = 130
mask = []
for i in range(256):
    if i < threshold:
        mask.append(0)
    else:
        mask.append(1)
img = img.point(mask, '1')
img.save('base64-masked.png')

captcha = pytesseract.image_to_string(img, lang='eng', config='--psm 8')
captcha = re.sub(r'\s+', '', captcha)
print(captcha)