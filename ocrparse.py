from PIL import Image, ImageFilter, ImageEnhance
import pytesseract
import os

# Set the path for Tesseract if it's not in the PATH environment variable
# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'

# Function to perform OCR on an image file


def perform_ocr(image_path):
    # Open the image file
    with Image.open(image_path) as image:
        # Convert the image to grayscale
        image = image.convert('L')

        # Increase the contrast of the image
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(2)

        # Sharpen the image
        image = image.filter(ImageFilter.SHARPEN)

        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(
            image, lang='eng', config='--oem 3 --psm 11')

        return text


# Main program starts here
if __name__ == "__main__":
    image_path = 'DATASTORE/NHL/ACTIONNETWORK/AN-NHL.png'
    ocr_output = perform_ocr(image_path)

    # Define the file path where the OCR results will be saved
    file_path = os.path.join("DATASTORE/NHL/ACTIONNETWORK", 'AN-NHL.txt')

    # Write the OCR results to a file
    with open(file_path, 'w') as file:
        file.write(ocr_output)
