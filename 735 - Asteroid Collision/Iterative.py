#132ms, 14.6MB

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        index = 0
        while(index < len(asteroids) - 1):
            if(asteroids[index] > 0 and asteroids[index+1] < 0):
                if(asteroids[index] > -asteroids[index+1]):
                    del asteroids[index+1]
                    continue
                elif(asteroids[index] == -asteroids[index+1]):
                    del asteroids[index+1]
                    del asteroids[index]
                else:
                    del asteroids[index]
                index = index - 1 if index > 0 else 0
            else:
                index += 1                       
        return asteroids