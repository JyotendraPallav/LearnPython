''' Program to read Images '''
from matplotlib import pyplot as plt
from skimage import data
from skimage.feature import blob_dog
from math import sqrt
from skimage.color import rgb2gray
import glob
from skimage.io import imread


example_file=glob.glob("D:\Github\Python Tutorial\LearnPython\pic1.jpg")[0]
im=imread(example_file, as_grey=True)
plt.imshow(im,cmap=None)
plt.show()

