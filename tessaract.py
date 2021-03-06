import pytesseract
import PIL.Image
import cv2

"""
Page segementation modes:
    0 = Orientation and script detection (OSD) only.
    1 = Automatic page segmentation with OSD.
    2 = Automatic page segmentation, but no OSD, or OCR.
    3 = Fully automatic page segmentation, but no OSD. (Default)
    4 = Assume a single column of text of variable sizes.
    5 = Assume a single uniform block of vertically aligned text.
    6 = Assume a single uniform block of text.
    7 = Treat the image as a single text line.
    8 = Treat the image as a single word.
    9 = Treat the image as a single word in a circle.
    10 = Treat the image as a single character.
    11 = Sparse text. Find as much text as possible in no particular order.
    12 = Sparse text with OSD.
    13 = Raw line. Treat the image as a single text line,
            bypassing hacks that are Tesseract-specific.
"""

"""
Tesseract OCR Engine:
    0 = Original Tesseract only.
    1 = Neural nets LSTM only.
    2 = Tesseract + LSTM.
    3 = Default, based on what is available.
"""
myconfig = r'--oem 3 --psm 4'

# main OCR image to string functionality
def img_to_string(file_name):
    text = pytesseract.image_to_string(PIL.Image.open(file_name), config=myconfig)
    return text

# TODO lines that parses and draws the output on the test image
def img_to_boxes(file_name):
    pytesseract.image_to_boxes(PIL.Image.open(file_name), config=myconfig)
    

if __name__ == '__main__':
    print(img_to_string('test.png'))