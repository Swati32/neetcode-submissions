class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for i in range(len(strs)):
            sorted_word = "".join(sorted(strs[i], key=str.lower))
            if sorted_word in words:
                words[sorted_word].append(strs[i])
            else:
                words[sorted_word] = [strs[i]]

        result = []
        for key,value in words.items():
            result.append(value)

        return result