import math
import numpy as np
from PIL import Image
from skimage import transform
from skimage import img_as_float
import matplotlib.pyplot as plt
from skimage import data
from scipy.ndimage import map_coordinates

def shift_up10_left20(xy):
     return xy - np.array([-20, 10])[None, :]

image = data.astronaut().astype(np.float32)
coords = transform.warp_coords(shift_up10_left20, image.shape)
warped_image = map_coordinates(image, coords)
print(warped_image)