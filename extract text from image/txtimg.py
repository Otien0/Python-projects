import pytesseract
from PIL import Image 

pytesseract.pytesseract.tesseract_cmd="/usr/share/tesseract-ocr/4.00/tessdata"
'''here it failed to work due to linux permission denied
errors which I'couldn't solve'''
#it worked so well on windows

img=Image.open('image.jpg')
text=pytesseract.image_to_string(img)
print(text)
