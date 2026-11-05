class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = 0
        left =0
        maxlen=0
        seen=set()
        if len(s)==1:
            return 1
        elif len(s)==0:
            return 0
        seen.add(s[0])
        while left<=right and right < len(s)-1:
            right +=1
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
                

            seen.add(s[right])

            maxlen= max(maxlen,right-left+1)
        return maxlen