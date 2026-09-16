class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count task frequencies 
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        # Step 2: Max-heap stores available tasks by remaining count (negated)
        heap = [-count for count in freq.values()]
        heapq.heapify(heap)

        # Step 3: Cooldown queue holds: (remaining_count, available_at_time)
        cooldown = deque()
        time = 0

        while heap or cooldown:
            time += 1

            if heap:
                count = 1 + heapq.heappop(heap)
                if count != 0:
                    cooldown.append((count, time + n))

            if cooldown and cooldown[0][1] == time:
                heapq.heappush(heap, cooldown.popleft()[0])
            
        return time 
                

        

        