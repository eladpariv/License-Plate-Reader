import easyocr

reader = easyocr.Reader(['en'], gpu=False)

def license_complies_format(text):
    """
    Check if the license plate text complies with the required format.

    Args:
        text (str): License plate text.

    Returns:
        bool: True if the license plate complies with the format, False otherwise.
    """
    if ((len(text) == 8 and
        (text[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and
        text[1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and
        text[2] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and
        text[3] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and
        text[4] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and
        text[5] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and
        text[6] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and
        text[7] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])) or

        (len(text) == 7 and
        (text[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and
          text[1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and
          text[2] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and
          text[3] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and
          text[4] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and
          text[5] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and
          text[6] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']))):
        return True
    else:
        return False

def read_license_plate(license_plate_crop):
    """
    Read the license plate text from the given cropped image.

    Args:
        license_plate_crop (PIL.Image.Image): Cropped image containing the license plate.

    Returns:
        tuple: Tuple containing the formatted license plate text and its confidence score.
    """
    detections = reader.readtext(license_plate_crop)
    for detection in detections:
        bbox, text, score = detection
        print(text)

        text = text.replace(' ', '').replace('.', '').replace(':', '').replace('/', '').replace('_', '')
        if license_complies_format(text):
            return text, score

    return None, None

