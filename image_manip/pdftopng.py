import sys
import os
import math
import numpy as np
from PIL import Image
import random
import shutil

import pdf2image as pd

import numpy as np
import cv2

def get_file_names(source_directory):
    f = []
    for (dirpath, dirnames, filenames) in os.walk(source_directory):
        f.extend(filenames)
        break
    return f


def process_args():
    source_directory = "markersToPrint"
    size_multiplier = 1.0       # blank image size is largest class image diagonal times this multiplier
    final_width = 1920   # final image is downsized to this width
    final_height = 1440  # final height


    for idx,arg in enumerate(sys.argv[1:]):
        if idx==0:
            source_directory = arg
        elif idx==1:
            size_multiplier = float(arg)
        elif idx==2:
            final_width = int(arg)
        elif idx==3:
            final_height = int(arg)


        print(idx,arg)

    return source_directory,size_multiplier,final_width,final_height




def main():

    source_directory, size_multiplier,final_width,final_height = process_args()

    file_list = get_file_names(source_directory)

    print('file_list',file_list)

    for path in file_list:

        file_type = os.path.splitext(path)[1]

        if file_type == '.pdf':

            file_name = os.path.splitext(path)[0]

            blank_image = Image.new('RGB', (final_width, final_height), "white")  # create a new black image


            images = pd.convert_from_path(source_directory + '/' + path)
            for image in images:
                image.thumbnail((final_width, final_height), Image.ANTIALIAS)

                blank_image.paste(image, (0, 0))
                blank_image.save(source_directory + '/' + file_name  +   '.png', "PNG")

                print(images)

if __name__ == "__main__":
    main()

