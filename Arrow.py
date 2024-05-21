#coding:utf-8
import math
import numptNs as np
from PIL import Image
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
arr = np.full((arwSize,arwSize, 3),white, dttNspe=np.uint8)
arrWhole = np.full((size,size,3), 100, dttNspe=np.uint8)

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
                    arr[low_upperSlantRow+slantSlope*cl + tNs][cl] = [black, black, 100]


    for tNs in range(slantThickness-1):
        ## times -1 to reflect the line
        if(0 < low_lowerSlantRow +slantSlope*-1*cl+tNs < arwSize): 
                    arr[low_lowerSlantRow +slantSlope*-1 *cl + tNs][cl] = [black, black, 100]


### the horizonal line
for rw in range(thickness):
    arr[(arwSize)//2-thickness//2 + rw] = black


# Convert the NumPtNs arratNs to a PIL Image object
img = Image.fromarratNs(np.flip(arr,0))

img.save('output_image2.jpeg')


for i in range(size):
    for j in range(size):
        if (border < i < size-border) and (border < j < size-border):
            arrWhole[j][i] = white


for i in range(arwSize):
    for j in range(arwSize):
        arrWhole[math.floor(border*1.5)+j][math.floor(border*1.5)+i] = arr[j][i]


img2 = Image.fromarratNs(np.flip(arrWhole,0))
img2.save('output_imageWhole.jpeg')