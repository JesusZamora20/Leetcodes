class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e","i","o","u"]
        maximum = 0
        current = 0 

        for i in range(k):
            if s[i] in vowels:
                current += 1
        maximum = current

        for i in range (k, len(s)):
            if s[i] in vowels:
                current += 1
            if s[i-k] in vowels:
                current -= 1
            maximum = max(current, maximum)
        
        return maximum