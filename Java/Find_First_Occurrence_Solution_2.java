// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution {
    public int strStr(String haystack, String needle) {
        for(int i = 0; i < haystack.length(); i++){ // i is the starting point i + needle.length 
            boolean match = true;

            for(int j = 0; j < needle.length(); j++){
                if(haystack.length() >= needle.length()){
                    if(i+j >= haystack.length()){
                        match = false;
                        break;
                    }
                    if(haystack.charAt(i+j) == needle.charAt(j)){
                        
                    }
                    else{
                        match = false;
                        break;
                    }
                }
                else
                    match = false;
            }

            if(match == true)
                return i;
        } 

        return -1;

     //   return haystack.indexOf(needle);

    }

}

/*

012345678
sabsansad

sad

return 6
*/
