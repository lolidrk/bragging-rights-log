class Solution {
public:
    int majorityElement(vector<int>& nums) {
        if (nums.size() == 1)
            return nums[0];
        unordered_map<int, int> count;
        for (int num: nums){
            count[num]++;
            if (count[num] > (nums.size()/2))
                return num;
        }
        return 0;
    }
};class Solution {
public:
    int majorityElement(vector<int>& nums) {
        if (nums.size() == 1)
            return nums[0];
        unordered_map<int, int> count;
        for (int num: nums){
            count[num]++;
            if (count[num] > (nums.size()/2))
                return num;
        }
        return 0;
    }
};
