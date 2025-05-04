class Solution {
public:
    
    int maxProfit(vector<int>& prices) {
    int min_price  = prices[0];
    int max_profit = 0;
    int profit_today = 0;
    for (const int price: prices){
        if (price < min_price) min_price = price;
        profit_today = price - min_price;
        if (profit_today > max_profit) max_profit = profit_today;
    }
    return max_profit;
    }
};

