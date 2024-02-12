from ultralytics import YOLO
import cv2
from util import read_license_plate

image_path = './Test images/testImage6.png'
frame = cv2.imread(image_path)

model = YOLO('last.pt')

threshold = 0.25

results = model(frame)[0]

for result in results.boxes.data.tolist():
    x1, y1, x2, y2, score, class_id = result

    license_plate_crop = frame[int(y1) - 30  :int(y2) + 30  , int(x1) -30 : int(x2) + 30, :]
    license_plate_crop_gray = cv2.cvtColor(license_plate_crop, cv2.COLOR_BGR2GRAY)
    _, license_plate_crop_thresh = cv2.threshold(license_plate_crop_gray, 64, 255, cv2.THRESH_BINARY_INV)
    license_plate_text, license_plate_text_score = read_license_plate(license_plate_crop_thresh)

    if score > threshold:
        cv2.rectangle(frame, (int(x1) , int(y1) ), (int(x2) , int(y2) ), (0, 255, 0), 4)
        cv2.putText(frame, license_plate_text, (int(x1), int(y1 - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

# Display the resulting image
cv2.imshow('Detection', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

