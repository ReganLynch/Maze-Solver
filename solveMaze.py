import sys
from mazeImageProcessor import *
from os import path


def main():
    #check that the file path was passed
    if len(sys.argv) != 2:
        print('invalid number of arguments passed')
        print('usage: solveMaze.py <file_path>')
        exit()
    file_path = str(sys.argv[1])
    #check if the passed file is valid
    if not path.exists(file_path):
        print('invalid file path')
        exit()
    #check that the input file is a .bmp
    file_name, file_extension = path.splitext(file_path)
    if(file_extension != '.bmp' and file_extension != '.BMP'):
        print('invalid file path')
        exit()
    #create a maze image processor object
    imageProcessor = mazeImageProcessor(path.abspath(file_path))


if __name__ == '__main__':
    main()
