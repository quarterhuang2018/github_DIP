# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 22:43:14 2020

@author: poww
"""

import numpy

##
# class DisjointSet
#
#   This class implements the methods for DisjointSet
##
class DisjointSet():
    ##
    # DisjointSet::constructor()
    #
    #   do nothing
    ##
    def __init__(self):
        pass
    
    ##
    # DisjointSet::find()
    #
    #   find the representative of this set, this is, the minimum value 
    ##
    def find(self, x):
        if(self.parents[x] != x):
            self.parents[x] = self.find(self.parents[x])
        
        return self.parents[x]
    
    ##
    # DisjointSet::makeSet()
    #
    #   create n single item sets from {0}, {1}, ....{n-1}
    ##
    def makeSet(self, n):
        self.parents = numpy.arange(0, n, dtype=numpy.int32)
    

    ##
    # DisjointSet::union()
    #
    #   union the two sets
    ##
    def union(self, x, y):
        # find the representative
        xset = self.find(x)
        yset = self.find(y)

        if(xset < yset):
            self.parents[yset] = xset           
        elif(xset > yset):
            self.parents[xset] = yset