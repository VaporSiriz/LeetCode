#include <vector>
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        vector<int> lNums, rNums;
        int i, size=nums.size();
        int result = -1;
        for(i=0;i<size;i++) {
            lNums.push_back(nums[i]);
            rNums.push_back(nums[i]);
        }
        for(i=1;i<size;i++) {
            lNums[i] += lNums[i-1];
        }
        for(i=size-2;i>=0;i--) {
            rNums[i] += rNums[i+1];
        }
        if(size==1 || rNums[1]==0)
            return 0;
        for(i=1;i<size-1;i++) {
            if(lNums[i-1] == rNums[i+1]) {
                return i;
            }
        }
        if(lNums[size-2]==0)
            return size-1;
        return -1;
    }
};

// [-1,-1,1,1,0,0] -> 5(O), 4(E)
// [-1,-1,0,0,-1,-1] -> 3(O), 2(E)
// [-1,-1,0,1,1,-1] -> 4(O), 0
// [0] -> run time error, 0

/*
    답안지
    class Solution {
    public int pivotIndex(int[] nums) {
        int sum = 0, leftsum = 0;
        for (int x: nums) sum += x;
        for (int i = 0; i < nums.length; ++i) {
            if (leftsum == sum - leftsum - nums[i]) return i;
            leftsum += nums[i];
        }
        return -1;
    }
}
    for (int x: nums) sum += x;
    if(leftsum == sum - leftsum - nums[i]) return i;
    leftsum += nums[i];

    leftsum | num[i] | rightsum
    sum = SUM[num[i]]([i=0,size])
    rightsum = sum - leftsum - nums[i]

    if(i==0) -> 0 ?= sum-0-nums[0]
    if(i==size-1) -> leftsum(sum-) ?= sum-leftsum-num

*/