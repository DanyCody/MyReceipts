from PIL import Image

MAX_LENGTH = 1024000


def save(image, name, length):
    print("type Image : " + str(type(image)))
    print("Length img : " + str(length))
    print("Name img : " + name)

    if length > MAX_LENGTH:
        print("The size of the image is too big")
        image = reduce(image, length)
    imagename = "img/Compressed_" + name
    image.save(imagename, optimize=True, quality=95)
    return imagename


def reduce(image, length):
    ratio = length / MAX_LENGTH
    print("Image must be reduced by : " + str(ratio))
    w, h = image.size
    print("Width : " + str(w) + ", Heigth : " + str(h))
    if w > h:
        image = image.rotate(-90, expand=True)
        reducedimage = image.resize((int(h / ratio), int(w / ratio)), Image.ANTIALIAS)
    else:
        reducedimage = image.resize((int(w / ratio), int(h / ratio)), Image.ANTIALIAS)

    return reducedimage
