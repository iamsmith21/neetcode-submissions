class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0; 

        for (int i = 0; i<prices.length;i++){
            int temp = 0;
            int start = i;
            int end = prices.length - 1;
            while (start < end){
                if ((prices[start] > prices[end]) && (prices[start] > prices[start+1])){
                    start++;

                } else {
                    temp = prices[end] - prices[start];
                    if (temp > profit) profit = temp;
                    end--;
                }
            }
        }   
        return profit;
    }
}
