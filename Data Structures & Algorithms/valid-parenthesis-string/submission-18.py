class Solution:
    def checkValidString(self, s: str) -> bool:
        normal = []
        ast = []
        
        for n in range(len(s)):
            if s[n] == "(":
                normal.append(n)
            elif s[n] == "*":
                ast.append(n)
            elif s[n] == ")":
                if normal:
                    normal.pop()
                elif ast:
                    ast.pop()
                else:
                    return False
                    
        # Cleanup: Match remaining '(' with '*' ensuring ast index > normal index
        while normal:
            if not ast:
                return False
                
            ast_ind = ast.pop()
            norm_ind = normal.pop()
            
            if ast_ind < norm_ind:
                return False
                
        return True