import pytesseract

'''Results differ between pytesseract in command line and code.
https://stackoverflow.com/questions/47995993/pytesseract-results-different-from-tesseract-command-line-results
'''

class OCR:
    __TESSERACT_PARAMS = '--oem 3 --psm 6'
    __TESSERACT_LANG='por'
    
    @classmethod
    def image_to_text(cls, img):
        text = pytesseract.image_to_string(img, lang=cls.__TESSERACT_LANG, config=cls.__TESSERACT_PARAMS)
        return text
