// https://leetcode.com/problems/valid-parentheses/

import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> container = new Stack<>();

        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '(' || s.charAt(i) == '{' || s.charAt(i) == '[')
                container.push(s.charAt(i));
            else{
                if(container.empty() == true)
                    return false;
                    
                if(s.charAt(i) == ')' && container.peek() != '(')
                    return false;
                if(s.charAt(i) == '}' && container.peek() != '{')
                    return false;
                if(s.charAt(i) == ']' && container.peek() != '[')
                    return false;
                container.pop();
            }
        }

        if(container.empty() == false)
            return false;
        else
            return true;
    }
}
