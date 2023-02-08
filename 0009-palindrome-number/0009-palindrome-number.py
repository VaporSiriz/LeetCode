class Solution:
    # 알고리즘
    """
        if num < 0:
            return False
        if 자릿수가 홀수:
        mid = num_of_digits/2
        
    """
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        str_x = str(x)
        start, end = 0, len(str_x)-1
        while start<=end:
            if str_x[start]!=str_x[end]:
                return False
            start += 1
            end -= 1
        return True
        