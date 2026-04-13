class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        posTime = [(position[i],(target-position[i])/speed[i]) for i in range(n)]
        posTime.sort(reverse=True)

        fleet = 0
        lastTime = 0

        for pos,time in posTime:
            if time>lastTime:
                fleet+=1
                lastTime=time
        
        return fleet