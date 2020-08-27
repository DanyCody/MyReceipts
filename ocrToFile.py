from PIL import Image
from PIL import ImageEnhance
import cv2
import requests
import io
import json
import numpy


def ocr(image):
    open_cv_image = numpy.array(image)
    # Convert RGB to BGR
    open_cv_image = open_cv_image[:, :, ::-1].copy()

    # Ocr
    url_api = "https://api.ocr.space/parse/image"

    _, compressedimage = cv2.imencode(".jpg", open_cv_image, [1, 90])
    file_bytes = io.BytesIO(compressedimage)

    result = requests.post(url_api,
                           files={r'C:\Users\Geoffrey\Desktop\Python\Text_1.png': file_bytes},
                           data={"apikey": "fb6f75e9b088957", "scale": "true", "isTable": "true"})

    result = result.content.decode()
    result = json.loads(result)

    text_detected = result.get("ParsedResults")[0].get("ParsedText")

    return text_detected
    # print(text_detected)


#    f = open(r'C:\Users\Geoffrey\Desktop\Python\Json\Cora_1.json', "a")
#    f.write("CONTRAST : " + contrast + "\n")
#    f.write(text_detected)
#    f.close()

