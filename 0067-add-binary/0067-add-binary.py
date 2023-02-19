class Solution:
    def addBinary(self, a: str, b: str) -> str:
        index = -1
        len_a = len(a)
        len_b = len(b)
        carry = 0
        sum_of_bin = ""
        while len_a+index>=0 or len_b+index>=0:
            bin_a = int(a[index]) if len_a+index>=0 else 0
            bin_b = int(b[index]) if len_b+index>=0 else 0
            sum = bin_a+bin_b+carry
            carry = int(sum/2)
            sum_of_bin = str(sum%2) + sum_of_bin
            index -= 1
        sum_of_bin = "1"+sum_of_bin if carry==1 else sum_of_bin
        return sum_of_bin