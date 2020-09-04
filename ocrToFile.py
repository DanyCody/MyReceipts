import requests
import json


def ocr(name):
    # Ocr
    url_api = "https://api.ocr.space/parse/image"

    with open(name, 'rb') as f:
        result = requests.post(url_api,
                               files={"img/Compressed_image_Car1.jpg": f},
                               data={"apikey": "fb6f75e9b088957", "scale": "true", "isTable": "true"})

    result = result.content.decode()
    result = json.loads(result)

    print("result : " + str(result))
    if result is None or result.get("ParsedResults")[0] is None:
        text_detected = result
    else:
        text_detected = result.get("ParsedResults")[0].get("ParsedText")

    return text_detected
