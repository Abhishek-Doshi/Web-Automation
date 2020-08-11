from googlesearch import search 
import pytesseract
from PIL import Image
import cv2
from web import open_web_page

tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'
TESSDATA_PREFIX= 'C:\\Program Files\\Tesseract-OCR'
tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'

def google_search(query, results = 1):
    urls = [print(url) for url in search(query, tld="co.in", num=results, stop=results, pause=2)]
    return urls

img = Image.open(r'C:\Users\\Home\Desktop\ARD.png')
#img = cv2.imread(r'C:\Users\\Home\Desktop\ARD.png')
#img = cv2.bitwise_not(img)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#img = Image.fromarray(img)


#query = 'python code for prime numbers'
#web = open_web_page(google_search(query))
print(pytesseract.image_to_string(img, config=tessdata_dir_config))