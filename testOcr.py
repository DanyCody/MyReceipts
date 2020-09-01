from PIL import Image
import numpy as np
import ocrToFile
import io


""" Load image from path. Return a numpy array """
#img = Image.open("img/image_Car1.jpg")
#img = img.resize((1512,2016), Image.ANTIALIAS)
#img = img.resize((756,1008), Image.ANTIALIAS)
#img.save('img/Compressed_image_Car1.jpg', optimize=True, quality=95)
#img = Image.open("img/image_Car1.jpg")
#print("Original Image : " + str(len(img.tobytes())))
#img = img.resize((504,378))
#img.save('img/Compressed_image_Car1.jpg')
img = Image.open("img/Compressed_image_Car1.jpg")
#print("Resized Image : " + str(len(img.tobytes())))
#tstimage = open("img/Compressed_image_Car1.jpg", 'rb')

res = ocrToFile.ocr(img)
print(res)


#return np.asarray(image) / 255