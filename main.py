import anvil.server
from PIL import Image
from PIL import ImageEnhance

anvil.server.connect("VAQPKXKNKSSD4HYOAGS2NZER-H3E7QJIUC62EZ43O")


@anvil.server.callable
def hello_world():
    return 'Hello World!'


@anvil.server.callable
def image_info(img):
    print("call ok")
    image = Image.frombytes('RGBA', (128, 128), img.get_bytes(), 'raw')

    return 'Image type : ' + str(type(image))


anvil.server.wait_forever()