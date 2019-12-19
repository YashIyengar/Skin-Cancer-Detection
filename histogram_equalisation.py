
from IPython.display import display, Math, Latex
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

import cv2
data_dir = 'D:/Python use case practice/Skin Cancer/New folder/HAM'
def get_histogram(image, bins):
    #array with size of bins, set to zeros
    histogram = np.zeros(bins)
   
    #loop through pixels and sum up counts of pixels
    for pixel in image:
        histogram[pixel] += 1
       
    #return our final result
    return histogram

#create our cumulative sum function
def cumsum(a):
    a = iter(a)
    b = [next(a)]
    for i in a:
        b.append(b[-1] + i)
    return np.array(b)


def histO(fileName):
   
    img = Image.open(data_dir + '/' + fileName)

    img = np.asarray(img)

    flat = img.flatten()


    hist = get_histogram(flat, 256)


    #execute the fn
    cs = cumsum(hist)


# numerator & denomenator
    nj = (cs - cs.min()) * 255
    N = cs.max() - cs.min()

# re-normalize the cdf
    cs = nj / N
    cs = cs.astype('uint8')
    img_new = cs[flat]
# put array back into original shape since we flattened it
    img_new = np.reshape(img_new, img.shape)
    return img_new


target_dir = 'F:/Skin Cancer/pracc/Histo_Equalised'
#os.mkdir(target_dir)
for i in os.listdir(data_dir):
    histoIm = histO(i)
    cv2.imwrite(target_dir + '/'+ i , histoIm)