class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for source, dest, time in times:
            adj[source].append((time, dest))
        
        min_heap = [(0, k)]
        shortest = {}

        while min_heap:
            time, dest = heapq.heappop(min_heap) 
            if dest in shortest:
                continue
            shortest[dest] = time

            for ntime, neighbor in adj[dest]:
                if neighbor not in shortest:
                    heapq.heappush(min_heap, (time + ntime, neighbor)) 
        
        return max(shortest.values()) if len(shortest) == n else -1

        