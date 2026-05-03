class Solution {
    public int characterReplacement(String s, int k) {
        int[] freq = new int[26];
        int maxFreq = 0;
        int left = 0;
        int res = 0;
        // correct windows size = (right -left +1) - maxFreq = 1

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            freq[c - 'A'] += 1;
            maxFreq = Math.max(maxFreq, freq[c - 'A']);

            while ((right - left + 1) - maxFreq > k) {
                freq[s.charAt(left) - 'A']--;
                left++;
            }
            res = Math.max(res, right - left + 1);
        }

        return res;
    }
}
