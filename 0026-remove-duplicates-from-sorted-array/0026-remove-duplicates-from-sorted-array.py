class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        sorted_numbers = []
        set_of_nums = set([])
        for num in nums:
            if num not in set_of_nums:
                set_of_nums.add(num)
                sorted_numbers.append(num)
        for i in range(0, len(sorted_numbers)):
            nums[i] = sorted_numbers[i]
                
        return len(set_of_nums)