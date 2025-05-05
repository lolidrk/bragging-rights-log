class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int total_profit = 0;
        int cur_price = prices[0];
        for (int i = 0; i < prices.size();++i){
            if (cur_price > prices[i]) cur_price = prices[i];
            profit = prices[i] - cur_price;
            if (profit > 0) {
                total_profit += profit;
                cur_price = prices[i];
            }
        }
        return total_profit;
    }
};
