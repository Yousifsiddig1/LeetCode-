https://leetcode.com/problems/sort-characters-by-frequency/description/?envType=daily-question&envId=2024-02-07
class Solution:
    def frequencySort(self, s: str) -> str:
        char_freq = {}
        
        for i in s:
            char_freq[i] = char_freq.get(i, 0) + 1

        sortChar= sorted(s, key=lambda x: (char_freq[x], x), reverse=True)
        res= ''.join(sortedChar)

        return res

            

        
