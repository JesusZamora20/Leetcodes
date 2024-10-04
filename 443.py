# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 00:26:47 2024

@author: jberm
"""

#443

class Solution(object):
    def compress(self, chars):
        s = ""
        ans = []
        l = 1
        for i in range(len(chars)-1):
            if chars[i] == chars[i+1]:
                l += 1
            else:
                if l == 1:
                    s += chars[i]
                    l = 1
                else:
                    s += chars[i] + str(l)
                    l = 1
        if l == 1:
            s += chars[len(chars)-1]
        else:
            s += chars[len(chars)-1] + str(l)  

        print(s)