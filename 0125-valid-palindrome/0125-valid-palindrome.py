class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_set = set([chr(n) for n in range(97, 97+26)] + [chr(n) for n in range(48, 58)])
        alpha_s = ""
        s = s.lower()
        for alpha in s:
            if alpha in alpha_set:
                alpha_s += alpha
        #print(alpha_s)
        length =len(alpha_s)
        for i in range(0, length):
            #print(f"{alpha_s[i]} != {alpha_s[-i-1]}")
            if alpha_s[i] != alpha_s[length-i-1]:
                return False
        return True