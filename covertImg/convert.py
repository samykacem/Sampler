import imageio
import os


directorySource = '../png/'
directoryDestination = '../gif/'
images = []

for filename in os.listdir(directorySource):
    im = imageio.imread(directorySource+filename)
    imageio.imwrite(directoryDestination+filename.replace(".png",".gif"), im)