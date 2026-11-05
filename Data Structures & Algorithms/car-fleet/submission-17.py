class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # position + speed*time = target 
        # time = (target - postion) // speed 
        # edge case= what if euqal positons have equal hours? - All the values of position are unique. = one car? 


        fleets=1
        times =defaultdict(int)
        t =[]
        for p in range(len(position)):
            time = float((target-position[p]))/speed[p]
            times[position[p]] = time
        timess=dict(sorted(times.items(), reverse=True))
        for time in timess.values():
            if t:
                
                if time > t[-1]:
                    fleets +=1
                    t.append(time)
            
            else:
                t.append(time)

        return fleets
        
