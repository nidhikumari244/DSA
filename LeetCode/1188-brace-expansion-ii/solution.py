class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """

        self.expr = expression
        self.pos = 0
        result = self.parseUnion()
        return sorted(result)
    
    def parseUnion(self):
        groups = [self.parseConcat()]
        while self.pos < len(self.expr) and self.expr[self.pos] == ',':
            self.pos += 1  # skip comma
            groups.append(self.parseConcat())
        
        result = set()
        for g in groups:
            result |= g
        return result
    
    def parseConcat(self):
        result = {""}
        while self.pos < len(self.expr) and self.expr[self.pos] not in ',}':
            term = self.parseTerm()
            result = {a + b for a in result for b in term}
        return result
    
    def parseTerm(self):
        if self.expr[self.pos] == '{':
            self.pos += 1  
            inner = self.parseUnion()
            self.pos += 1  
            return inner
        else:
            ch = self.expr[self.pos]
            self.pos += 1
            return {ch}
        
