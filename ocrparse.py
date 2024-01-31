from PIL import Image
import pytesseract

# Function to perform OCR on an image file


def perform_ocr(image_path):

    image = Image.open(image_path)

    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(image)

    return text


# Main program starts here
if __name__ == "__main__":

    image_path = 'full_screenshot.png'

    ocr_output = perform_ocr(image_path)

    with open('AN-NHL.txt', 'w') as file:
        file.write(ocr_output)

    # Send off ActionNetwork data to ML before next refresh

    # print(ocr_output)
