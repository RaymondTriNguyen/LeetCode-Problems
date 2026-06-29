// https://leetcode.com/problems/length-of-last-word/

import java.util.ArrayList;

class Solution {
    public int lengthOfLastWord(String s) {
        String temp = "";
        ArrayList<String> words = new ArrayList<>();

        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) != ' ')
                temp += s.charAt(i);
            else{
                if(temp.length() != 0)
                    words.add(temp);
                temp = "";
            }
        }
        if(temp.length() != 0){
            words.add(temp);
            temp = "";
        }

        String last = words.get(words.size() - 1);
        return last.length();
    }
}
