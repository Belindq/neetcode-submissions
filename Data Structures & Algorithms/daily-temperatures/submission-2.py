class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        indices=[]
        indices.append(0)
        for i in range(1,len(temperatures)):
            while indices:
                index= indices[-1]
                if temperatures[i]>temperatures[indices[-1]]:
                    index=indices.pop()
                    result[index]=i-index
                elif temperatures[i]<=temperatures[index]: 
                    break
            indices.append(i)    
            
        return result