// https://leetcode.com/problems/sqrtx/description/

class Solution {
    public int mySqrt(int x) {
        long low = 0;
        long high = x;
        long answer = 0;
        while(low <= high){
            long mid = (low + high) / 2;

            if(mid * mid <= x){
                low = mid + 1;
                answer = mid;
            }
            else
                high = mid - 1;
        }

        return (int) answer;
    }
}
