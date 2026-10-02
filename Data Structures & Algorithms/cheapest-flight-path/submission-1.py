class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for source, destination, cost in flights:
            adj[source].append((destination, cost))
        
        q = deque([(src, 0)])
        min_cost = [math.inf] * n
        min_cost[src] = 0

        stops = 0
        while q and stops <= k:
            for i in range(len(q)):
                stop, cost = q.popleft()

                for neighbor, ncost in adj[stop]:
                    cost_to_reach_neighbor = cost + ncost
                    if min_cost[neighbor] > cost_to_reach_neighbor:
                        min_cost[neighbor] = cost_to_reach_neighbor
                        q.append((neighbor, cost_to_reach_neighbor))
                
            stops += 1

        return  min_cost[dst] if min_cost[dst] != math.inf else -1
