class Solution:
    def longestPalindrome(self, s: str) -> int:
        selections = {}
        for alphabat in s:
            if alphabat not in selections:
                selections[alphabat] = 0
            selections[alphabat] += 1

        length = 0
        odd_flag = False
        #print(selections)
        for value in selections.values():
            if value%2==1:
                odd_flag = True
            if value>1:
                length += value if value%2==0 else value-1

        return length+(1 if odd_flag else 0)
