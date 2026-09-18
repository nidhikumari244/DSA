class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
        

        intervals = []
        
        for c in first:
            start = first[c]
            end = last[c]
            i = start
            valid = True
            while i <= end:
                ch = s[i]
                if first[ch] < start:

                    valid = False
                    break
                end = max(end, last[ch])
                i += 1
            
            if valid:
                intervals.append((start, end))
        

        intervals.sort(key=lambda x: (x[1], x[1] - x[0]))
        
        result = []
        prev_end = -1
        for start, end in intervals:
            if start > prev_end:
                result.append(s[start:end + 1])
                prev_end = end
        
        return result