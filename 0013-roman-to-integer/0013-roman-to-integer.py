class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numbers = {
            "I" : 1,
            "IV": 4,
            "V" : 5,
            "IX": 9,
            "X" : 10,
            "XL" : 40,
            "L" : 50,
            "XC": 90,
            "C" : 100,
            "CD" : 400,
            "D" : 500,
            "CM": 900,
            "M" : 1000
        }
        sum_of_nums = 0
        length = len(s)
        i = 0
        while i < length:
            if s[i:i+2] in roman_numbers:
                sum_of_nums += roman_numbers[s[i:i+2]]
                i += 2
            else:
                sum_of_nums += roman_numbers[s[i]]
                i += 1
                
        return sum_of_nums