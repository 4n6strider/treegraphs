#-------------------------------------------------------------------------------
# Name:        tree-graph 1
# Author:      4n6strider
# Copyright:   (c) 4n6strider
#-------------------------------------------------------------------------------

import networkx as nx  #reading: http://networkx.github.io/documentation/latest/reference/drawing.html
import csv   #reading: https://docs.python.org/2/library/csv.html
import openpyxl   #reading: http://openpyxl.readthedocs.org/en/2.3.3/
#import xlswriter


def get_edgelist(efile):
    with open(raw_input("Paste absolute path to the file: "), 'rb') as efile:
        csv_efile=csv.reader(efile,dialect="excel")
        edgelist=[]
        for row in csv_efile:
            #edgelist.append(tuple(row['source'], row['target'])) /// this needs to be fixed to get list fo tuples :source:target:
            
            edgelist.append(row) # this returns data in format: list of values like:['source;target'], ['qradar-offense-39793;39793']
             
        return edgelist
        
    
      


efile=""
get_edgelist(efile)
