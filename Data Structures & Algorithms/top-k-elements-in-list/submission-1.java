class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int n : nums) {
            freq.put(n, freq.getOrDefault(n, 0) + 1);
        }

        List<Integer> keys = new ArrayList<>(freq.keySet());
        // System.out.println(keys);
        keys.sort((a, b) -> freq.get(b) - freq.get(a));

        int[] res = new int[k];

        for (int i = 0; i < k; i++) {
            res[i] = keys.get(i);
        }

        return res;
    }
}
