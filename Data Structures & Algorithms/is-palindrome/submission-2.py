class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        clean = ''.join([i for i in s if i.isalnum()])
        start =0
        end = len(clean)-1
        while start< len(clean)/2:
            if clean[start]!=clean[end]:
                return False
            start+=1
            end-=1
        return True