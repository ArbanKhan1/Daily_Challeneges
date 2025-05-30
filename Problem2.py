class Solution:    
    def ValidCorner(self,mat): 
        rows = len(mat)
        if rows == 0:
            return False
            
        cols = len(mat[0])
        seen = set()
        
        for row in mat:
            ones = []
            for i in range(cols):
                if row[i] == 1:
                    ones.append(i)
            for i in range(len(ones)):
                for j in range(i+1, len(ones)):
                    pair = (ones[i], ones[j])
                    if pair in seen:
                        return True
                    seen.add(pair)
        return False