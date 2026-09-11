from itertools import permutations

class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        valid_numbers = set()
        
        for perm in permutations(digits, 3):
            hundreds, tens, ones = perm
            
            if hundreds == 0:          
                continue
            if ones % 2 != 0:         
                continue
            
            number = hundreds * 100 + tens * 10 + ones
            valid_numbers.add(number)
        
        return len(valid_numbers)
