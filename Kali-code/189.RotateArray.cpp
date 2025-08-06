class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> result(n);
        for (int i = 0; i < nums.size(); i ++){
            result[((i+k)%nums.size())] = nums[i];
        }

        nums = result;
    }
};
