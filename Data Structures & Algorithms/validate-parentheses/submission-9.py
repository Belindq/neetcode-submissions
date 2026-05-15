class Solution:
    def isValid(self, s: str) -> bool:
        pairs={
            ')':'(',
            '}':'{',
            ']':'['
        }
        seen=deque()
        if len(s)%2!=0:
            return False
        
        for i in s:
            if i in pairs: 
                if seen and pairs[i]==seen[-1]:
                    seen.pop()
                else:
                    return False
            else:
                seen.append(i)
        return len(seen)==0

