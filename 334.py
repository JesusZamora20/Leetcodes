# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 00:19:48 2024

@author: jberm
"""

#334 
class Solution(object):
    def increasingTriplet(self, nums):
        res = False

        for i in range(0,len(nums)-2,1):
            if nums[i] < nums[i+1] < nums[i+2]:
                res = True
