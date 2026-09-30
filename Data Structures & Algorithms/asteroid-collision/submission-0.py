class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for a in asteroids:
            # Fight until a collision is no longer possible
            while stack and stack[-1] > 0 and a < 0:
                diff = stack[-1] + a  # e.g., 10 + (-5) = 5 (stack wins)

                if diff < 0:
                    stack.pop()       # Stack loses, incoming fights next in line
                elif diff == 0:
                    stack.pop()       # Draw: both explode
                    break
                else:
                    break             # Stack wins: incoming explodes
            else:
                stack.append(a)       # Survived with no collisions or beat everyone

        return stack

        

        