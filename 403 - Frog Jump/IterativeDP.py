#248ms, 16.5MB
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        tracker = {
            0: set()
        }
        tracker[0].add(1)
        
        for i in range(len(stones) - 1):
            if stones[i] not in tracker:
                continue
            for jump in tracker[stones[i]]:
                reach = stones[i] + jump
                if reach not in tracker:
                    tracker[reach] = set()
                if reach == stones[-1]:
                    return True
                tracker[reach].add(jump + 1)
                tracker[reach].add(jump)
                if jump - 1 > 0:
                    tracker[reach].add(jump-1)
                    
        return False