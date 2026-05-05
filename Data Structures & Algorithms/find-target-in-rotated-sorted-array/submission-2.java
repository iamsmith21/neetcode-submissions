class Solution {
    public int search(int[] nums, int target) {
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

        int pivot = left;

        left = 0;
        right = len - 1;

        if (target >= nums[pivot] && target <= nums[right]) {
            left = pivot;
        } else {
            right = pivot - 1;
        }

        while (left <= right) {
            int mid = (left + right) / 2;

            if (nums[mid] == target)
                return mid;
            else if (nums[mid] < target)
                left = mid + 1;
            else
                right = mid - 1;
        }

        return -1;
    }
}
