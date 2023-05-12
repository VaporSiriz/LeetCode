class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bin_search(s:int, e:int) -> int:
            middle = s+(e-s)//2
            if s>=e:
                return -1
            print(f"nums[{s}:{e}] = {nums[s:e]}, middle-{middle} : {nums[middle]} ?= target-{target}")
            if nums[middle] == target:
                return middle
                
            if nums[middle] < target:
                print('r')
                return bin_search(middle+1, e)
            else:
                print('l')
                return bin_search(s, middle)
            
        init_index = bin_search(0, len(nums))
        #print(f"init_index : {init_index}")
        l_index = init_index
        r_index = init_index
        #print(f"left")
        while True:
            index = bin_search(0, l_index)
            if index==-1:
                break
            l_index = index
        if l_index == -1:
            l_index = init_index
        #print(f"l_index : {l_index}")
        #print(f"right")
        while True:
            index = bin_search(r_index+1, len(nums))
            if index==-1:
                break
            r_index = index
        if r_index == -1:
            r_index = init_index
        #print(f"r_index : {r_index}")
        
        return [l_index, r_index]
                