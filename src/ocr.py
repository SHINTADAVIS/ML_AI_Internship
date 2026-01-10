import cv2
import numpy as np
import pytesseract
from PIL import Image
from difflib import SequenceMatcher
from fpdf import FPDF

def get_string(img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    result = pytesseract.image_to_string(Image.open(img_path))
    return result

def calculate_accuracy(original, predicted):
    return SequenceMatcher(None, original, predicted).ratio() * 100

if __name__ == "__main__":
    image_path = "data/test_image.png"
    actual_text = "PRESIDENT KENNEDY TODAY"

    print("OCR Started...\n")
    extracted_text = get_string(image_path)
    print("Recognized Text:\n", extracted_text)

    accuracy = calculate_accuracy(actual_text, extracted_text)
    print(f"Accuracy: {accuracy:.2f}%")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, extracted_text)
    pdf.output("output.pdf")

    print("\nResult saved as output.pdf")
