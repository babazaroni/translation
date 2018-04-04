#!/usr/bin/env python

import sys
import os
import math
import numpy as np
from PIL import Image
import random
import shutil

import numpy as np
import cv2

def get_file_names(source_directory):
    f = []
    for (dirpath, dirnames, filenames) in os.walk(source_directory):
        f.extend(filenames)
        break
    return f

def process_args():
    source_directory = "."
    final_width = 1920    # final image is downsized to this height,width
    final_height = 1440

    for idx,arg in enumerate(sys.argv[1:]):
        if idx==0:
            source_directory = arg
        elif idx==1:
            size_multiplier = float(arg)
        elif idx==2:
            final_width_height = int(arg)
        elif idx==3:
            class_count = int(arg)


        print(idx,arg)

    return source_directory,final_width, final_height


def main():

    source_directory,final_width,final_height = process_args()

    file_list = get_file_names(source_directory)

    print('file_list',file_list)


    dest_name = "resized"

    dest_dir = source_directory + '/' + dest_name

    shutil.rmtree(dest_dir, ignore_errors=True)
    os.makedirs(dest_dir)

    for path in file_list:

        fullpath = source_directory + '/' + path
        try:
            img = Image.open(fullpath).convert('LA')
        except:
            continue

        print("processing:",fullpath)

        file_name = os.path.splitext(path)[0]

        width_scale = final_width / img.size[0]
        height_scale = final_height / img.size[1]
        final_scale = min(width_scale,height_scale)


        blank_image = Image.new('L', (final_width, final_height), "black")  # create a new black image

        print(img.size)

        final_size = (int(final_scale * img.size[0]),int(final_scale * img.size[1]))

        print(final_size)

#        img.thumbnail(final_size,Image.ANTIALIAS)
        img = img.resize(final_size, Image.ANTIALIAS)

        print(img.size)

        blank_image.paste(img, (0, 0))

        blank_image.save(dest_dir + '/' + file_name  +   '.png', "PNG")

#        img.show()





#        cv2.imshow("", blank_image)
#        cv2.waitKey(0)
#        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
