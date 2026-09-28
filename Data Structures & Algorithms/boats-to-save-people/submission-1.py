class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0
        while left <= right:
            sum = people[left] + people[right]
            if sum <= limit:
                boats += 1
                left += 1
                right -= 1
            elif people[right] <= limit:
                boats += 1
                right -= 1
            elif people[left] <= limit:
                boats += 1
                left += 1

        return boats



        