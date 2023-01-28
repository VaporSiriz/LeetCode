class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        length = len(nums)
        for i in range(0, length):
            if nums[i] not in numbers:
                numbers[nums[i]] = []
            numbers[nums[i]].append(i)

        for number, indexes in numbers.items():
            index1 = indexes.pop()
            sub = target-number
            if sub in numbers and len(numbers[sub])>0:
                index2 = numbers[sub].pop()
                return sorted([index1, index2])

        return []