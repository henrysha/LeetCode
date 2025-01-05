"""
735. Asteroid Collision
Medium

We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

Constraints:

- 2 <= asteroids.length <= 104
- -1000 <= asteroids[i] <= 1000
- asteroids[i] != 0
"""

class Solution:
    def checkCollision(self, a: int, b: int) -> bool:
        return a * b < 0

    def collide(self, a: int, b: int) -> int:
        if a == -b:
            return None
        return a if abs(a) > abs(b) else b

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ret = []

        for i, asteroid in enumerate(asteroids):
            if not ret or asteroid > 0:
                ret.append(asteroids[i])
                continue
            survive = True
            for j in range(len(ret) - 1, -1, -1):
                if not self.checkCollision(asteroid, ret[j]):
                    break
                result = self.collide(asteroid, ret[j])
                if not result:
                    survive = False
                    ret.pop()
                    break
                if result != asteroid:
                    survive = False
                    break
                ret.pop()
            if survive:
                ret.append(asteroid)
        
        return ret