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