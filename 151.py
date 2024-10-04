# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 00:26:08 2024

@author: jberm
"""

#151

class Solution(object):
    def reverseWords(self, s):
        words = []
        word = ""

        for i in s:
            if not i.isspace():
                word += i
            elif i.isspace():
                words.append(word)
                word = ""
        words.append(word)
        words.reverse()

        wordsrev = [x for x in words if x]

        return " ".join(wordsrev)