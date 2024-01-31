from PIL import Image
import pytesseract
import os

# Function to perform OCR on an image file


def perform_ocr(image_path):

    image = Image.open(image_path)

    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(image)

    return text


# Main program starts here
if __name__ == "__main__":

    image_path = 'DATASTORE/NHL/ACTIONNETWORK/AN-NHL-CAPTURE.png'

    ocr_output = perform_ocr(image_path)

    file_path = os.path.join("DATASTORE/NHL/ACTIONNETWORK", 'AN-NHL.txt')
with open(file_path, 'w') as file:
    file.write(ocr_output)

    # Send off data to ML before next refresh

    # print(ocr_output)
