import cv2
import pytesseract
from PIL import Image
import numpy as np
import json
from pdf2image import convert_from_path
import PyPDF2
import io

class eOnsightExtracter:
    """This is the eOnsightExtracter class.
    This class takes an image as input and gives a JSON file as output with extracted information."""

    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(self.image_path).convert("RGB")

    def preprocess_image(self):
        """Converts the image to grayscale, applies thresholding and histogram equalization."""
        gray_image = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2GRAY)
        equalized_image = cv2.equalizeHist(gray_image)
        _, binary_image = cv2.threshold(equalized_image, 150, 255, cv2.THRESH_BINARY_INV)
        return binary_image

    def text_extracter(self):
        """Extracts text from the preprocessed image using pytesseract."""
        preprocessed_image = self.preprocess_image()
        data = pytesseract.image_to_data(Image.fromarray(preprocessed_image), lang='eng', output_type=pytesseract.Output.DICT)
        extracted_data = []
        for i in range(len(data['level'])):
            entry = {
                'text': data['text'][i],
                'left': data['left'][i],
                'top': data['top'][i],
                'width': data['width'][i],
                'height': data['height'][i],
                'confidence': data['conf'][i]
            }
            extracted_data.append(entry)
        return extracted_data

    def to_json(self):
        """Converts the extracted data to JSON format."""
        data = self.text_extracter()
        json_data = json.dumps(data, indent=4)
        return json_data

    def image_to_pdf(self):
        """Converts the image to PDF."""
        self.image.save("output.pdf", "PDF")

    def pdf_to_text(self):
        """Extracts text from the PDF using PyPDF2."""
        pdf_file = open('output.pdf', 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)  # Updated to PdfReader
        page = pdf_reader.pages[0]  # Updated to access pages attribute
        text = page.extract_text()  # Updated to extract_text() method
        return text

# Example
if __name__ == "__main__":
    image_path = '/content/Extrait_IQOA_data.png'  # Path to the input image
    extractor = eOnsightExtracter(image_path)
    
    # Convert image to PDF
    extractor.image_to_pdf()
    
    # Extract text from image and save to JSON
    json_data = extractor.to_json()
    with open('extracted_data.json', 'w') as json_file:
        json_file.write(json_data)
    
    # Extract text from PDF
    pdf_text = extractor.pdf_to_text()
    print(pdf_text)
