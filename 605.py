# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 00:24:43 2024

@author: jberm
"""

#605

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        f = [0] + flowerbed + [0]

        for i in range(1, len(f) - 1):
            if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
                f[i]==1
                n -= 1
        return n <= 0