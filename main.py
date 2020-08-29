import anvil.server
import ocrToFile
from PIL import Image
import io
from PIL import ImageEnhance

anvil.server.connect("VAQPKXKNKSSD4HYOAGS2NZER-H3E7QJIUC62EZ43O")

@anvil.server.callable
def hello_world():
    return 'Hello World!'


@anvil.server.callable
def image_info(img):
    print("call ok")
    print("Type Img : " + str(type(img)))
    print("Format img : " + img.content_type)

    #image = Image.frombytes('RGBA', (128, 128), img.get_bytes(), 'raw')
    image = Image.open(io.BytesIO(img.get_bytes()))
    print("File Size In Bytes:- " + str(len(image.fp.read())))

    res = ocrToFile.ocr(image)
    # res = ocrToFile.ocr(img.get_bytes())
    print(res)
    return 'Image type : ' + res

anvil.server.wait_forever()