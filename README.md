# eOnsightExtracter

eOnsightExtracter est une classe Python permettant d'extraire des informations textuelles d'une image et de les sauvegarder au format JSON. Elle permet également de convertir des images en PDF et d'extraire du texte de ces PDF.

## Installation

Sur Google Colab, vous pouvez installer les dépendances nécessaires en exécutant les commandes suivantes :

!pip install opencv-python-headless pytesseract Pillow numpy pdf2image PyPDF2
!apt-get install tesseract-ocr

## Dépendances

Ce projet dépend des bibliothèques Python suivantes :

- cv2
- pytesseract
- PIL
- numpy
- json
- pdf2image
- PyPDF2
- io


## Features

- **Image Preprocessing**: Converts images to grayscale, applies thresholding, and histogram equalization.
- **Text Extraction**: Uses `pytesseract` to extract text from preprocessed images.
- **JSON Output**: Converts extracted text data to JSON format.
- **Image to PDF**: Converts images to PDF format.
- **PDF Text Extraction**: Extracts text from PDFs using `PyPDF2`.

## Requirements

- Python 3.x
- OpenCV
- Pytesseract
- PIL (Pillow)
- NumPy
- json
- pdf2image
- PyPDF2

## Installation

Install the required packages using pip:

```sh
pip install -r requirements.txt
