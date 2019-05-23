from PIL import Image
import numpy as np

w, h = 512, 512
data = np.zeros((h, w, 3)).astype(np.uint8)

data[:256, :] = [255, 255, 255]
img = Image.fromarray(data, 'RGB')
img.save('my.png')
