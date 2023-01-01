#include <vector>
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int i, size=nums.size(), leftsum=0, sum=0;
        for(i=0;i<size;i++) sum += nums[i];
        for(i=0;i<size;i++) {
            if(leftsum == sum - leftsum - nums[i]) return i;
            leftsum += nums[i];
        }
        return -1;
    }
}