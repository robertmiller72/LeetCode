#92ms, 19.3MB

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        target = stones[-1]
        stones = set(stones)
        cache = dict()
        
        def jump(val, j):
            if val == target:
                return True
            
            if val not in stones:
                return False
            
            if (val, j) in cache:
                return cache[(val, j)]
            
            if jump(val+j+1, j+1):
                cache[(val, j)] = True
                return True
            
            if jump(val+j, j):
                cache[(val, j)] = True
                return True
            
            if j - 1 > 0:
                cache[(val, j)] = jump(val+j-1, j-1)
                return cache[(val, j)]
            
            cache[(val, j)] = False
            return False
        
        return jump(1, 1)