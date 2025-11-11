# TCS iON RIO-125 :Automate extraction of handwritten text from an image
# Project Overview
This project was developed as part of the TCS iON RIO 125 Remote Internship program, a part of Certified Specialist in Machine learning and Artificial Intelligence program by ICT Academy of Kerala in association with Kerala Knowledge Economy Mission (KKEM). 

This project demonstrates an **automated handwritten text extraction and recognition system** using **Tesseract OCR**, **OpenCV**, and **Python**.  
The workflow includes image preprocessing, OCR-based recognition, accuracy evaluation, and automatic PDF generation of recognized text.

The aim of this project is to automatically **detect, clean, and extract handwritten text** from an input image, and convert the recognized content into a structured text output or a PDF file.  
It is implemented in **Google Colab**, utilizing **Google Drive** for dataset storage and access.

# Tools and Libraries Used
| Tool / Library                            | Version                                     | Description 
|----------------                           |----------                                   |-------------
| **Tesseract OCR**                         | 4.1.3                                       | Optical Character Recognition engine for text extraction 
| **Leptonica**                             | 1.79.0                                      | Image processing library used internally by Tesseract 
| **OpenCV (cv2)**                          | Latest                                      | Used for image preprocessing (grayscale, dilation, erosion) 
| **NumPy**                                 | Latest                                      | Array operations and kernel creation 
| **Pillow (PIL)**                          | Latest                                      | Image I/O operations for Tesseract 
| **FPDF**                                  | 1.7.2                                       | PDF generation for recognized text output 
| **difflib**                               | Built-in                                    | Used for similarity and accuracy calculation 
| **Google Colab + Drive**                                                                | Cloud-based execution and dataset storage 

 # Workflow
 
 ### 1. Mount Google Drive
 # Access the image dataset from Google Drive:

from google.colab import drive
drive.mount('/content/drive')
filename = '/content/drive/MyDrive/Test_image.png'

### 2. Image Preprocessing

### Enhance the image for better OCR accuracy:
import cv2, numpy as np
img = cv2.imread(filename)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.ones((1, 1), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)
cv2.imwrite("removed_noise.png", img)

### 3.Text Extraction using Tesseract

from PIL import Image
import pytesseract

def get_string(img_path):
    return pytesseract.image_to_string(Image.open(img_path))

text = get_string(filename)
print("Recognized Text:\n", text)

### 4. Generate PDF of Recognized Text

from fpdf import FPDF
pdf = FPDF(format='letter')
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.write(5, text)
pdf.output("Recognized_Text.pdf")

### 5. Accuracy Evaluation

from difflib import SequenceMatcher

ground_truth = "PRESIDENT KENNEDY TODAY"
def similar(a, b):
    return str(SequenceMatcher(None, a, b).ratio() * 100) + "%"

accuracy = similar(ground_truth, text)
print("Recognition Accuracy:", accuracy)

### Dataset Details
Type: Handwritten text images
Format: PNG/JPEG
Source: Custom uploaded image (Test_image.png) from Google Drive

## Content Example: Handwritten phrase "PRESIDENT KENNEDY TODAY"

## To enhance performance, you can expand this dataset with more samples of different handwriting styles and qualities.

## Example Output
## Input Image (Expected Text):
PRESIDENT KENNEDY TODAY

## Recognized Output:
“PRESIDENI KENNEDY botany

## Recognition Accuracy:
68.0%

### Installation & Requirements
## Install all required dependencies:

!apt install tesseract-ocr
!pip install pytesseract opencv-python pillow fpdf

## Confirm Tesseract installation:
!tesseract --version

## Future Enhancements

# Integration of deep learning-based OCR models (e.g., CRNN, TrOCR, EasyOCR)

# Dataset expansion with labeled handwritten text samples

# GUI interface for real-time handwritten text recognition

# Multi-language handwriting support

