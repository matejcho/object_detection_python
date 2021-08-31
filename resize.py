from PIL import Image
import os, sys
import glob

root_dir = "C:\\Users\\Matej Gjozinski\\PycharmProjects\\object_detection\\data\\images\\"

for filename in glob.iglob(root_dir + '**/*.jpg', recursive=True):
    print(filename)
    im = Image.open(filename)
    imResize = im.resize((416, 416), Image.ANTIALIAS)
    imResize.save(filename, 'PNG', quality=90)
