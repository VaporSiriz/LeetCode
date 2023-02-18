class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        dict_of_nums = {}
        for num in nums:
            if num == val:
                continue
            if num not in dict_of_nums:
                dict_of_nums[num] = 0
            dict_of_nums[num] += 1
        index = 0
        for num, count in dict_of_nums.items():
            for i in range(0, count):
                nums[index] = num
                index += 1
        return index               