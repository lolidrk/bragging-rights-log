class Solution {
public:
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        unordered_map <int,int> counts;
        for (auto& vec : dominoes){
            int num = std::min(vec[0], vec[1]) * 10 + std::max(vec[0], vec[1]); 
            counts[num]++;
        }
        int result = 0;
        for (auto& pair : counts){
            if (pair.second > 1) result += (pair.second * (pair.second - 1)) / 2;
        }
        return result;
    }
};
