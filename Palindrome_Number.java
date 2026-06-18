// https://leetcode.com/problems/palindrome-number/

class Solution {
    public boolean isPalindrome(int x) {
        String str = String.valueOf(x);
        String palindrome = "";
        for(int i = str.length() - 1; i >= 0; i--)
            palindrome += str.charAt(i);
        if(palindrome.equals(str))
            return true;
        else
            return false;
    }
}
