# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 00:24:24 2024

@author: jberm
"""

#1431

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        res = []
        for i in candies:
            res.append(i + extraCandies >= max(candies))
        return res