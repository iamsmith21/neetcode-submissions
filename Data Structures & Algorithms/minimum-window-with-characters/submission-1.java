class Solution {
    public String minWindow(String s, String t) {
        int minLen = Integer.MAX_VALUE;
        int startIndex = -1;

        
        HashMap<Character, Integer> map = new HashMap<>(256);
            for (int j = 0; j < t.length() ; j++){
                char c = t.charAt(j);
                map.put(c, map.getOrDefault(c,0) + 1);
            }

            int count = 0;
            int i = 0;
            for (int j=0; j< s.length(); j++){
                char charAtJ = s.charAt(j);
                if (map.getOrDefault(charAtJ, 0) > 0) {
                    count++;
                }

                map.put(charAtJ, map.getOrDefault(charAtJ, 0) -1);

                //shrinking the window until its valid... 
                while (count == t.length()) {
                    if (j - i + 1 < minLen) {
                        minLen = j - i + 1;
                        startIndex = i;
                    }

                char leftChar = s.charAt(i);
                if (map.containsKey(leftChar)){
                    map.put(leftChar, map.get(leftChar) + 1);
                    if (map.get(leftChar) > 0){
                        count--;
                    }
                }
                i++;
                }
            }

        return startIndex == -1 ? "" : s.substring(startIndex, startIndex + minLen);
    }
}
