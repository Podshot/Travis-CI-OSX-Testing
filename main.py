import os
import sys
import numpy
import pygame
from pygame import image
import PIL
import OpenGL

try:
    import ftputil
except ImportError: # We can skip this since the module is now options
    pass

def main():
    #pygame.init()
    directory = getattr(sys, '_MEIPASS', None)
    if directory:
        with open(os.path.join(directory, 'log.txt'), 'w') as out:
            out.write("Extended support: {}".format(image.get_extended()))
    else:
        with open('log.txt', 'w') as out:
            out.write("Extended support: {}".format(image.get_extended()))
    print "Has extended image support:", pygame.image.get_extended()
    print ""
    raw_input("Press enter to close...")

if __name__ == '__main__':
    main()
