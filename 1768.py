# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 00:15:23 2024

@author: jberm
"""

#1768 merge strings alternately

class Solution(object):
    def mergeAlternately(self, word1, word2):
        i, j = 0,0
        res = ""
        
        while i < len(word1) and j < len(word2):
            res += word1[i]
            res += word2[j]
            i += 1
            j += 1
        res += word1[i:]
        res += word2[j:]
        
        return res 