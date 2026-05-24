class Solution:

    def encode(self, strs: List[str]) -> str:
        send=''
        for item in strs:
            send+=str(len(item))+'#'
            send+=(item)
        return send



    def decode(self, s: str) -> List[str]:
        decoded=[]
        point=0
        length=''
        while point < len(s):
            if s[point]!='#':
                length += (s[point])
                point +=1
            else:
                decoded.append(s[point+1:point+1+int(length)])
                point+=int(length)+1
                length=''

        return decoded        
                 
