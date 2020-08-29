from PIL import Image
import numpy as np
import optimizeImage


""" Load image from path. Return a numpy array """
img = Image.open("img/image_Car1.jpg")
image = np.array(img)

w, h, d = image.shape
print('Image found with width: {}, height: {}, depth: {}'.format(w, h, d))

X = image.reshape((w * h, d))
K = 20  # the desired number of colors in the compressed image

colors, _ = optimizeImage.find_k_means(X, K, max_iters=2)
idx = optimizeImage.find_closest_centroids(X, colors)
idx = np.array(idx, dtype=np.uint8)
X_reconstructed = np.array(colors[idx, :] * 255, dtype=np.uint8).reshape((w, h, d))
compressed_image = Image.fromarray(X_reconstructed)
print("Compressed 1 File Size In Bytes:- " + str(len(compressed_image.read())))

#return np.asarray(image) / 255