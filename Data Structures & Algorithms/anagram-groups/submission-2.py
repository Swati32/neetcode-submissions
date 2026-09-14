class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for word in strs:
            sorted_word = "".join(sorted(word.lower()))
            words[sorted_word] = words.get(sorted_word, [])
            words[sorted_word].append(word)

        result = []
        for key,value in words.items():
            result.append(value)

        return result