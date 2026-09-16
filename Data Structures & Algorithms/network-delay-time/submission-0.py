class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
  
        for u, v, time in times:
            adj[u].append((v,time))
        
        min_heap = [(0, k)]
        shortest_time = {}

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in shortest_time:
                continue

            shortest_time[node] = time

            for neighbor, n_time in adj[node]:
                if neighbor not in shortest_time:
                    heapq.heappush(min_heap, (time + n_time, neighbor))
            
        return max(shortest_time.values()) if len(shortest_time) == n else -1 

            


        