# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 00:27:43 2024

@author: jberm
"""

# 11

class Solution(object):
    def maxArea(self, height: List[int]) -> int:
        maxwater = 0
        p1 = 0
        p2 = len(height) -1

        while p1 < p2:
            current_water = min([height[p1], height[p2]]) * (p2-p1)
            if current_water > maxwater:
                maxwater = current_water
            elif height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1
        return maxwater
