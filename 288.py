# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 00:19:09 2024

@author: jberm
"""

# Product of array except self. 

class Solution(object):
    def productExceptSelf(self, nums):
        res = []

        for i in range(len(nums)): 
            product = 1
            for j in range(len(nums)): 
                if i != j:
                    product *= nums[j]
            res.append(product)

        return(res)