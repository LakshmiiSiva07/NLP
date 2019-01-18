"""
Reading and Extracting Data
"""

import gzip
import sys

from lxml import etree

if __name__ == '__main__':

    for inputfile in sys.argv[1:]:
        with gzip.open(inputfile, 'rb') as f:
            tree = etree.parse(inputfile) #parse_tree
            root = tree.getroot()
            for child in root:
                if child.get('type') == 'story': #Finds docs of type story
                    for grandchild in child.findall('./TEXT/P'): #Finds all child with Text and P
                        if grandchild.text: #Filters empty paragraph
                            print grandchild.text
