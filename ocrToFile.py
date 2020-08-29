from PIL import Image
from PIL import ImageEnhance
import cv2
import requests
import io
import json
import numpy
import optimizeImage


def ocr(image):
    open_cv_image = numpy.array(image)
    w, h, d = open_cv_image.shape
    print('Image found with width: {}, height: {}, depth: {}'.format(w, h, d))

    X = open_cv_image.reshape((w * h, d))
    K = 20  # the desired number of colors in the compressed image

    colors, _ = optimizeImage.find_k_means(X, K, max_iters=2)
    idx = optimizeImage.find_closest_centroids(X, colors)
    idx = numpy.array(idx, dtype=numpy.uint8)
    X_reconstructed = numpy.array(colors[idx, :] * 255, dtype=numpy.uint8).reshape((w, h, d))
    compressed_image = Image.fromarray(X_reconstructed)
    print("Compressed 1 File Size In Bytes:- " + str(len(compressed_image.read())))

    # Convert RGB to BGR
    open_cv_image = open_cv_image[:, :, ::-1].copy()

    # Ocr
    url_api = "https://api.ocr.space/parse/image"

    _, compressedimage = cv2.imencode(".jpg", open_cv_image, [1, 90])
    file_bytes = io.BytesIO(compressedimage)
    print("Compressed 2 File Size In Bytes:- " + str(len(file_bytes.read())))

    result = requests.post(url_api,
                           files={r'C:\Users\Geoffrey\Desktop\Python\Text_1.png': file_bytes},
                           data={"apikey": "fb6f75e9b088957", "scale": "true", "isTable": "true"})

    result = result.content.decode()
    result = json.loads(result)

    print("result : " + str(result))
    if result is None or result.get("ParsedResults")[0] is None:
        text_detected = result
    else:
        text_detected = result.get("ParsedResults")[0].get("ParsedText")

    return text_detected
    # print(text_detected)


#    f = open(r'C:\Users\Geoffrey\Desktop\Python\Json\Cora_1.json', "a")
#    f.write("CONTRAST : " + contrast + "\n")
#    f.write(text_detected)
#    f.close()

