// https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        shortestLength = len(strs[0])

        for i in range(0, len(strs), 1):
            length = len(strs[i])
            if length < shortestLength:
                shortestLength = length

        for i in range(0, shortestLength):
            match = True

            for j in range(0, len(strs)):
                if j == 0:
                    character = strs[j][i]
                else:
                    if strs[j][i] != character:
                        match = False
                        break

            if match == True:
                prefix += strs[0][i]
            else:
                break
        
        return prefix
