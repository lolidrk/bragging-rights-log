class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        int nsize = nums.size();
        int initial;
        int finals;
        bool flag = true;
        vector<string> result;
        if (nsize == 0){
            return result;
        }
        if (nsize == 1) {
            result.push_back(to_string(nums[0]));
            return result;
        }
        for (int i = 1; i < nsize; i ++){
            if (nums[i-1] != (nums[i]-1)){
                if (!flag){
                    result.push_back(to_string(initial) + "->" + to_string(nums[i-1]));
                    flag = true; 
                }
                else{
                    result.push_back(to_string(nums[i-1])); 
                }
            }
            else {
                if (flag) {
                    initial = nums[i-1];
                    flag = false;
                }
            }
        }
        if (!flag){
            result.push_back(to_string(initial) + "->" + to_string(nums[nsize-1]));
        } else {
            result.push_back(to_string(nums[nsize-1]));
        }
        return result;
    }
};
