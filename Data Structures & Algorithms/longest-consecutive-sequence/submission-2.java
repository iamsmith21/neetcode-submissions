class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();

        for (int n : nums) {
            set.add(n);
        }

        int longest = 0;
        for (int num : set) {
            if (!set.contains(num - 1)) {
                int c = 1;

                while (set.contains(num + c)) {
                    c++;
                }

                longest = Math.max(longest, c);
            }
        }

        return longest;
    }
}
