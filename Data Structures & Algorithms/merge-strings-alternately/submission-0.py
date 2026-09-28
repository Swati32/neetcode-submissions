class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        idx1 = 0
        idx2 = 0
        
        while idx1 < len(word1) and idx2 < len(word2):
            result.append(word1[idx1]) 
            result.append(word2[idx2]) 
            idx1 += 1
            idx2 += 1

        result += word1[idx1:]
        result += word2[idx2:]
    
        return "".join(result)


        