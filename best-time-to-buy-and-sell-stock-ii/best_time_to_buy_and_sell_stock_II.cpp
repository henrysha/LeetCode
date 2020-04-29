class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0;
        bool transaction = false;
        int numberOfPrices = prices.size();
        int boughtPrice;
        for (int i = 0; i < numberOfPrices; i++){
            if (transaction) {
                // must sell or keep
                if (i == numberOfPrices-1){
                    // must sell since last element
                    transaction = false;
                    maxProfit += prices[i] - boughtPrice;
                } else if (prices[i+1] <= prices[i]){
                    // sell since current price is the best price
                    transaction = false;
                    maxProfit += prices[i] - boughtPrice;
                }
            } else {
                // must not do anything or buy
                if (i < numberOfPrices-1) {
                    // buy if the current price is lower than the next price
                    if (prices[i+1] > prices[i]){
                        transaction = true;
                        boughtPrice = prices[i];
                    }
                }
            }
        }
        return maxProfit;
    }
};