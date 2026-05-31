class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        for i in asteroids: 
            if mass >= i:
                mass = mass + i  

        if mass >= asteroids[len(asteroids)-1]:
            return True 
        else:
            return False 
        




    
