class Solution {
public:
    bool canJump(vector<int>& nums) {
        int horizon = 0;
        /**
        Here we basically try and see how far we can reach at each step 
        and the moment we are able to reach the end we just return true. 
        **/
        for (int i = 0; i < nums.size(); i ++)
        {
            if (horizon < i)
                return false;
            horizon = max(horizon, nums[i]+i);
            
            if ( i >= (nums.size() - 1) )
                return true;
        }
        return false;
    }
};

/** Question for reference 

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 
**/
