from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        feet = []
        car_info = []
        for i in range(len(position)):
            car_info.append([position[i], speed[i]])
        
        car_info.sort(reverse=True)
        for i in range(len(car_info)):
            p, s = car_info[i]
            feet.append((target - p) / s)
            if len(feet) >= 2 and feet[-1] <= feet[-2]:
                feet.pop()
    
        return len(feet)

    
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_info = []
        for i in range(len(position)):
            car_info.append([position[i], speed[i]])
        
        car_info.sort(reverse=True)
        current_time = (target - car_info[0][0]) / car_info[0][1]
        fleet = 1
        for i in range(1, len(car_info)):
            p, s = car_info[i]
            next_time = (target - p) / s
            if next_time > current_time:
                fleet += 1
                current_time = next_time
    
        return fleet



if __name__ == "__main__":
    # target = 12
    # position = [10, 8, 0, 5, 3]
    # speed = [2, 4, 1, 1, 3]
    # target = 10
    # position = [1,4]
    # speed = [3,2]
    sol = Solution()
    target=12
    position=[10,8,0,5,3]
    speed=[2,4,1,1,3]
    result = sol.carFleet(target, position, speed)
    print("Number of car fleets:", result)