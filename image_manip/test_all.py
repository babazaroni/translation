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
            final_width = int(arg)
        elif idx==3:
            final_height = int(arg)


        print(idx,arg)

    return source_directory,final_width, final_height


def main():

    source_directory,final_width,final_height = process_args()

    file_list = get_file_names(source_directory)

    for path in file_list:

        fullpath = source_directory + '/' + path
        try:
            img = Image.open(fullpath).convert('LA')
        except:
            continue

        os.system("/root/CCTag/build/src/applications/detection -n 3 -i " + fullpath)


#        img.show()





#        cv2.imshow("", blank_image)
#        cv2.waitKey(0)
#        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
