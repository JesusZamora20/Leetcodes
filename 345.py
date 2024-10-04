# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 00:24:57 2024

@author: jberm
"""

#345

class Solution(object):
    def reverseVowels(self, s):
        v = 'aeiouAEIOU'
        vowelsrev = [] #vowels of s reversed
        vrevindex = 0
        srev = ''   
        #iterate backwards the word
        for i in range(len(s),0,-1):
            if s[i-1] in v:
                vowelsrev.append(s[i-1])
        for i in s:
            if i in v:
                srev += vowelsrev[vrevindex]
                vrevindex += 1
            else:
                srev += i
        return srev