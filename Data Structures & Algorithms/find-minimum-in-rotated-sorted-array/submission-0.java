class Solution {
    public int findMin(int[] nums) {
         int len = nums.length;

        int right = len - 1;
        int left = 0;

        while (left < right) {
            int mid = (left + right) / 2;

            if (nums[right] > nums[mid]) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return nums[right];
    }
}
