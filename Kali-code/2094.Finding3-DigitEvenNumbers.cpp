class Solution {
public:
    vector<int> findEvenNumbers(vector<int>& digits) {
        vector<int> res;
        vector<int> freq(10,0);

        for (auto d : digits){
            freq[d]++;
        }

        for (int i = 1; i <= 9; ++i){
            if (freq[i] > 0){
                freq[i]--;
                for (int j = 0; j <= 9; ++j ){
                    if (freq[j] > 0){
                        freq[j]--;
                        for (int k = 0; k <= 9; ++k){
                            if (freq[k] > 0 && k%2 ==0){
                                res.push_back(i*100 + j *10 + k);
                            }
                        }
                        freq[j]++;
                    }
                }
                freq[i]++;
            }
        }

        sort(res.begin(), res.end());
        return res;

    }
};
