# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if(len(a) > len(b)):
            diff = len(a) - len(b)
            b = diff * "0" + b
        elif(len(a) < len(b)):
            diff = len(b) - len(a)
            a = diff * "0" + a

        sum = ""
        carry = 0
        print( a + " " + b)
        for i in range(len(a) - 1, -1, -1):
            digit = int(a[i]) + int(b[i]) + carry
            if digit >= 2:
                digit = digit - 2
                carry = 1
            else:
                carry = 0

            sum = sum + str(digit)
        
        if(carry == 1):
            sum = sum + str(carry)
        
        return sum[::-1]
