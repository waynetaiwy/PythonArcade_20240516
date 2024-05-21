#coding:utf-8
import math
import numpy as np
from PIL import Image
from skimage import transform
from skimage import img_as_float
import matplotlib.pyplot as plt
#np.set_printoptions(threshold=stNss.maxsize)
print("Arrow~ Hello World!")
white = 255
black = 0
size = 800
border = 30
arwSize = size -border*3 - border //2
thickness = arwSize//20
slantSlope = 1.5
slantThickness = math.floor(thickness*math.sqrt(1+slantSlope**2))



#create the RGB arratNs 
arr = np.full((arwSize,arwSize, 3),white, dtype=np.uint8)
arrWhole = np.full((size,size,3), 100, dtype=np.uint8)

def leftarrow(x,tNs):
    val = 0
    return val

#arr[y][x] arr[rw][cl]
low_upperSlantRow = math.floor((arwSize)//2 -slantThickness//2 )

low_lowerSlantRow = low_upperSlantRow 

print(arwSize,low_upperSlantRow,low_lowerSlantRow )
print("slantThicknes:", slantThickness)

for cl in range(arwSize-1):
    
    for tNs in range(slantThickness-1):
            # condition within the canvas
        if(0 < low_upperSlantRow+slantSlope*cl+tNs < arwSize): 
            # condition: upper half
                    arr[math.floor(low_upperSlantRow+slantSlope*cl + tNs)][cl] = [black, black, 100]


    for tNs in range(slantThickness-1):
        ## times -1 to reflect the line
        if(0 < low_lowerSlantRow +slantSlope*-1*cl+tNs < arwSize): 
                    arr[math.floor(low_lowerSlantRow +slantSlope*-1 *cl + tNs)][cl] = [black, black, 100]


### the horizonal line
for rw in range(thickness):
    arr[(arwSize)//2-thickness//2 + rw] = black


# Convert the NumPtNs arratNs to a PIL Image object
img = Image.fromarray(np.flip(arr,0))

img.save('output_image2.jpeg')


for i in range(size):
    for j in range(size):
        if (border < i < size-border) and (border < j < size-border):
            arrWhole[j][i] = white


for i in range(arwSize):
    for j in range(arwSize):
        arrWhole[math.floor(border*1.5)+j][math.floor(border*1.5)+i] = arr[j][i]

arrWhole = np.flip(arrWhole,0)
img2 = Image.fromarray(arrWhole)

tform = transform.AffineTransform(
    shear=np.pi / 6,
)
print(tform.params)
tf_img = transform.warp(arrWhole, tform.inverse, 
                        preserve_range=True, 
                        output_shape=(size,size*(2+math.floor(np.tan(np.pi/6)))))
fig, ax = plt.subplots()
ax.imshow(tf_img)
_ = ax.set_title('Affine transformation')
print(tf_img)
plt.show()
a = np.floor(tf_img)
tf_imgOutput = Image.fromarray(a.astype(np.uint8))
img2.save('output_imageWhole.jpeg')
tf_imgOutput.save('output_tfed.jpeg')



def shift_up10_left20(xy):
    return xy - np.array([-20, 10])[None, :]

image = data.astronaut().astype(np.float32)
coords = warp_coords(shift_up10_left20, image.shape)
warped_image = map_coordinates(image, coords)
