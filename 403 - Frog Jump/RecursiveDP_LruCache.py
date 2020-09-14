#68ms, 19.7MB

class Solution:
    from functools import lru_cache
    def canCross(self, stones: List[int]) -> bool:
        
        target = stones[-1]
        stones = set(stones)
        
        @lru_cache(maxsize=None)
        def jump(val, j):
            if val == target:
                return True
            
            if val not in stones:
                return False
            
            if j - 1 > 0:
                return jump(val+j+1, j+1) or jump(val+j, j) or jump(val+j-1, j-1)
            return jump(val+j+1, j+1) or jump(val+j, j)
        
        return jump(1, 1)