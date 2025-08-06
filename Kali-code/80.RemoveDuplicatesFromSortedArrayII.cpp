class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() <= 2) return nums.size();
        int k = 0;
        for (int i =0; i < nums.size(); i ++){
            if ( (k < 2) || nums[i] != nums[k-2]){
                nums[k++] = nums[i];
            }
        }
        return k;
    }
};
