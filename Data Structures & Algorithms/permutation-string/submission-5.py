class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        for i in s1:
            freq1[i] +=1
        left=0
        right =0
        if len(s2) ==1 and s1==s2:
            return True
        elif len(s2) ==1:
            return False
        freq2[s2[left]]+=1
        while right < len(s2)-1:
            print(freq2, freq1)
            if right-left+1 != len(s1):
                right +=1
                freq2[s2[right]]+=1
            else:
                if freq1!=freq2:
                    freq2[s2[left]] -=1
                    if freq2[s2[left]] ==0:
                        del freq2[s2[left]]
                    right +=1
                    freq2[s2[right]]+=1
                    left +=1
                else: 
                    return True
        if freq1==freq2:
            return True            
        return False

            

