class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq=defaultdict(int)
        length=1
        maxfreq=1
        maxlength=1
        left=0
        right =1
        if len(s)==1:
            return 1
        
        for right in range(len(s)):
            freq[s[right]]+=1
            maxfreq=max(maxfreq,freq[s[right]])
            if right-left+1 - maxfreq >k:
                freq[s[left]]-=1
                left +=1
            maxlength=max(maxlength, right-left+1)
                
                
        return maxlength