class Solution {
    public int maxArea(int[] heights) {
        
        int start = 0;
        int end = heights.length - 1;
        int h = 0;

        while (start < end){
            
            int temp = (end - start) * Math.min(heights[start],heights[end]);
            if (temp > h) h = temp;

            if (heights[start] < heights[end]){
                start++;
            } else {
                end--;
            }
        }
        return h;
    }
}
