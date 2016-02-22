#-------------------------------------------------------------------------------
# Name:        tree-graph 1
# Author:      4n6strider
# Copyright:   (c) 4n6strider
#-------------------------------------------------------------------------------

import networkx as nx  #reading: http://networkx.github.io/documentation/latest/reference/drawing.html
import csv   #reading: https://docs.python.org/2/library/csv.html
import openpyxl   #reading: http://openpyxl.readthedocs.org/en/2.3.3/
#import xlswriter


def get_nodelist(nfile):
    with open(raw_input("Paste absolute path to the file: "), 'rb') as nfile:
        csv_nfile=csv.reader(nfile,dialect="excel")
        nodelist=[]
        for row in csv_nfile:
            nodelist.append(row)
        return nodelist
        
    
      


nfile=""
get_nodelist(nfile)
