import cv2
import easyocr

cap = cv2.VideoCapture("dataset.mp4")
reader = easyocr.Reader(['en'], gpu=True)
plate_cascade = cv2.CascadeClassifier('license_plate.xml')
compare_output = ""
check_db = ""


def display_database():
    file = open('database.txt', 'r')
    line = file.read().splitlines()
    print("License plates in database:")
    if check_db != line:
        print(line)
        print("\n")


def check_database():
    file = open('database.txt', 'r')
    line = file.read().splitlines()
    return line


display_database()

while cap.isOpened():
    success, img = cap.read()
    if success is True:
        plate_img = img.copy()
        plate_rect = plate_cascade.detectMultiScale(plate_img, scaleFactor=2, minNeighbors=7)

        for (x, y, w, h) in plate_rect:
            cv2.rectangle(plate_img, (x, y), (x + w, y + h), (51, 51, 255), 3)
            imgCaptured = plate_img[y: y + h, x:x + w]

            cv2.imshow("Output", plate_img)
            result = reader.readtext(imgCaptured, detail=0)
            # print(result)
            plate_db = check_database()
            if set(result).intersection(plate_db):
                result_string = ' '.join(map(str, result))
                if compare_output == result_string:
                    continue
                else:
                    compare_output = result_string
                    print("Welcome " + compare_output + "\nGate opening\n")
            cv2.waitKey(1)
    else:
        print("Process finished")
        exit()

cap.release()
cv2.destroyAllWindows()
