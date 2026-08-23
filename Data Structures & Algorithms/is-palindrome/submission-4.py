class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1

        while start <= end:
            if s[start].isalnum() and s[end].isalnum():
                if s[start].lower() != s[end].lower():
                    return False
                else:
                    start+= 1
                    end -= 1
            elif not s[start].isalnum() and not s[end].isalnum():
                start+= 1
                end -= 1
            elif not s[start].isalnum():
                start +=1 
            else:
                end -=1
        return True