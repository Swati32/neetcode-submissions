class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        Greedy rule for boats: You must always give the heaviest person (right) a boat on every iteration. If the lightest person can squeeze in with them (people[left] + people[right] <= limit), advance left += 1. Either way, the heaviest person is accounted for (right -= 1).
        '''
        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0

        while left <= right:
            # If the lightest person can share the boat with the heaviest
            if people[left] + people[right] <= limit:
                left += 1
            
            # The heaviest person always takes this boat
            right -= 1
            boats += 1

        return boats


        