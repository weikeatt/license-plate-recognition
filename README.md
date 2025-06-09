# 🚗 License Plate Detection & Recognition
This project uses **OpenCV** for license plate detection and **EasyOCR** for optical character recognition (OCR) to extract and identify license plate text from images and videos. It supports multiple languages and includes a simple database verification system to enable automated gate access or alerting.
---

## 🔥 Features
- Detects license plates in images and video frames  
- Uses contour detection and Haar Cascade classifier for plate localization  
- Applies EasyOCR for accurate multi-language text recognition  
- Supports English and Simplified Chinese (customizable)  
- Crops and highlights license plate regions  
- Compares recognized plates against a stored database file (`database.txt`)  
- Prints welcome messages and simulates gate opening on recognized plates  
- Real-time video processing with OpenCV
---

## 🛠️ Requirements
- Python 3.x  
- OpenCV (`opencv-python`)  
- imutils  
- EasyOCR  
- Numpy  

Install dependencies with:
```bash
pip install opencv-python imutils easyocr numpy
