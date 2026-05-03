class Solution {

    public static String encode(List<String> strs) {
        String str = "";
        char delimeter = '#';

        for (int i = 0; i < strs.size(); i++) {
            int len = strs.get(i).length();
            str += "" + len + delimeter + strs.get(i);
        }

        return str;
    }

    public static List<String> decode(String str) {
        // 5#Hello5#World
        List<String> myList = new ArrayList<String>();

        int i = 0;
        int len = str.length();
        while (i < len) {
            int j = str.indexOf('#', i);

            int wordLen = Integer.parseInt(str.substring(i, j));

            String word = str.substring(j + 1, j + 1 + wordLen);
            myList.add(word);
            i = j + 1 + wordLen;
        }

        return myList;
    }
}
