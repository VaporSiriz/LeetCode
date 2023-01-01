from typing import List

def containsDuplicate(nums: List[int]) -> bool:
        nums_dict = {}
        flag = False
        for num in nums:
            if num in nums_dict:
                flag = True
                break
            nums_dict[num] = 1
        return "true" if flag else "false"

print(containsDuplicate([1,2,3,4]))