class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for word in strs:
            length = len(word)
            encoded += f"{length}#{word}"
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1

            length = s[i:j]
            start = j + 1
            end = j + int(length)

            decoded.append(s[start:end+1])
            i = end + 1
        return decoded
