class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_anagram, t_anagram = {alpha:0 for alpha in s}, {alpha:0 for alpha in t}
        for i in s:
            s_anagram[i] += 1
        for i in t:
            t_anagram[i] += 1
            
        return s_anagram == t_anagram