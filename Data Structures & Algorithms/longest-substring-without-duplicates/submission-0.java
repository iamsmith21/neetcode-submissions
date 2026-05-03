class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        int leftWin = 0;
        int rightWin = 0;
        int maxLen = 0;
        for (int i=0;i<s.length();i++){
            if (!map.containsKey(s.charAt(i))){
                map.put(s.charAt(i),i);
                rightWin++;
                maxLen = Math.max(maxLen, rightWin - leftWin);
            }
            else{
                if(map.get(s.charAt(i)) >= leftWin) {leftWin = map.get(s.charAt(i))+ 1;}
                map.put(s.charAt(i), i);
                rightWin++;
                maxLen = Math.max(maxLen, rightWin - leftWin);
            }
        }
        return maxLen;
    }
}
