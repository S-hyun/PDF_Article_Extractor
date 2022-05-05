import sys
from text import text
# -*- encoding: utf-8 -*-

from image import image
from table import table
import argparse

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Extract text, images, and tables at articles in pdf.')
    parser.add_argument('-f', '--file', 
                        type = str,
                        dest = 'file', 
                        help = 'File name to extract.')
    
    parser.add_argument('-t', '--text', 
                        dest = 'text', 
                        action = 'store_true', 
                        help = 'Extract text')
    
    parser.add_argument('-i', '--image', 
                        dest = 'image', 
                        action = 'store_true', 
                        help = 'Extract image')
    
    parser.add_argument('-a', '--table', 
                        dest = 'table', 
                        action = 'store_true', 
                        help = 'Extract table')
    args = parser.parse_args()
    if (args.text):
        print('text')
        text(args)
    if (args.image):
        print('image')
        image(args)
    if (args.table):
        print('table')
        table(args)
    print('345')
main()
print('123')
