from PIL import Image
import numpy as np
import ocrToFile


""" Load image from path. Return a numpy array """
#img = Image.open("img/image_Car1.jpg")
#img = img.resize((1512,2016), Image.ANTIALIAS)
#img = img.resize((756,1008), Image.ANTIALIAS)
#img.save('img/Compressed_image_Car1.jpg', optimize=True, quality=95)
img = Image.open("img/Compressed_image_Car1.jpg")
res = ocrToFile.ocr(img)
# res = ocrToFile.ocr(img.get_bytes())
print(res)


#return np.asarray(image) / 255