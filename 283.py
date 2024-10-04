# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 00:27:06 2024

@author: jberm
"""

#283
class Solution(object):
    def moveZeroes(self, nums):
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums