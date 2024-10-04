# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 00:27:43 2024

@author: jberm
"""

# 11

class Solution(object):
    def maxArea(self, height):
        
        maxwater = 0

        for p1 in range(len(height)):
            for p2 in range(len(height)):
                water = min([height[p1], height[p2]]) * (p2-p1)
                if water > maxwater: 
                    maxwater = water
        return maxwater
