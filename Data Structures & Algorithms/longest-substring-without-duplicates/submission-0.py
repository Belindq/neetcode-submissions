class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right =1
        left =0
        lenmax=0
        seen = set()
        if len(s)==0:
            return 0
        elif len(s)==1:
            return 1
        seen.add(s[left])
        while right<len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right +=1
            else:
                seen.remove(s[left])
                left +=1
                
            lenmax=max(lenmax, right-left)
                
        return lenmax
