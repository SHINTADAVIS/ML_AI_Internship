# Automate Extraction of Handwritten Text from an Image

**TCS iON Remote Internship RIO-125**  
Project developed as part of the **Certified Specialist in Machine Learning and Artificial Intelligence** program by **ICT Academy of Kerala** in association with **Kerala Knowledge Economy Mission (KKEM)**.

---

## Project Overview

This project extracts handwritten text from images using **OpenCV** and **Tesseract OCR**. 
Key features:
- Reads an image of handwritten or printed text.
- Applies preprocessing (grayscale, noise removal).
- Extracts text using Tesseract OCR.
- Calculates accuracy against expected text.
- Exports recognized text as a PDF.
 
## Installation

## 1. Clone the repository:

git clone https://github.com/SHINTADAVIS/ML_AI_Internship.git  

cd ML_AI_Internship  

## 2. Install Python dependencies:

pip install -r requirements.txt   

## 3. Install Tesseract OCR engine

### Ubuntu / Linux:

sudo apt install tesseract-ocr.

### Windows:  

Download installer from Tesseract GitHub  
Add Tesseract to your system PATH  

## Usage  

Run the Python script:  
python src/ocr.py  

Recognized text will be printed in the terminal.  
Accuracy will be calculated against the expected text.  
A PDF of the recognized text will be saved as output.pdf.  

## Sample Output  

Recognized Text:  
PRESIDENT KENNEDY TODAY  

Accuracy: 68.00%  



