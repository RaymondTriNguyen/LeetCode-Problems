# https://leetcode.com/problems/plus-one/submissions/2050452468/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[len(digits) - 1] != 9:
            digits[len(digits) - 1] = digits[len(digits) - 1] + 1
            return digits
        else:
            newDigits = []
            carry = 1

            for i in range(len(digits) - 1, -1, -1):
                digit = digits[i]
                currentDigit = digit + carry
                if(currentDigit > 9):
                    carry = 1
                    currentDigit = currentDigit - 10
                else:
                    carry = 0

                newDigits.append(currentDigit)
            
            if(carry == 1):
                newDigits.append(carry)
            
            return newDigits[::-1]
# 4 2 1 9
# 4 2 2 0
