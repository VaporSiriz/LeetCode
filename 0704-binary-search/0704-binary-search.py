class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        mid = start + int((end-start)/2)
        while start<=end:
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                end = mid-1
            else:
                start = mid+1
            mid = start + int((end-start)/2)
        return -1