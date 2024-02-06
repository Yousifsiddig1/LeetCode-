https://leetcode.com/problems/longest-common-prefix/description/
# Beats 95.43% , 30ms runtime
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        strs.sort()

        oneString = strs[0]
        twoString = strs[-1]

        comman = ""
        for i in range(len(oneString)):
            if i < len(twoString) and oneString[i] == twoString[i]:
                comman += oneString[i]
            else:
                break

        return comman
