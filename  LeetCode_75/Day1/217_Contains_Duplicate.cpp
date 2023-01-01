#include <map>
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int, int> nums_map;
        int i, size=nums.size();
        nums_map.insert({ nums[0], 1 });
        for(i=1;i<size;i++) {
            if(nums_map.find(nums) == nums_map.end())
                return true;
            nums_map.insert(nums[i], 1);
        }
        return false;

    }
};


/*
/*
map<string, int> mapset;
int main(void) {

	mapset.insert({ "Alice", 100 });
	mapset.insert({ "Bob", 200 });

	if (mapset.find("Alice") != mapset.end()) 
*/