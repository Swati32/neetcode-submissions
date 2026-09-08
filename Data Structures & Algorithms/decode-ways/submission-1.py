class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if not s or s[0]=='0':
            return 0
        
        prev_1 = 1
        prev_2 = 1

        for i in range(1, n):
            temp = prev_2
            curr = 0
            one_digit = int(s[i])
            if one_digit != 0:
                curr += prev_2

            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <=26:
                curr += prev_1
            
            prev_1 = temp 
            prev_2 = curr
            
            
        return prev_2
            
        