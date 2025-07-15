import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

def text_recognition(image_path):
  if os.path.exists(image_path):
    img = Image.open(image_path)
    result = pytesseract.image_to_string(img, lang = 'kor+eng')
    print(result)
    return result
  else:
    return None