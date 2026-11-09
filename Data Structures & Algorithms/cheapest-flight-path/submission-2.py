class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for source, destination, cost in flights:
            adj[source].append((destination, cost))
        
        q = deque([(src, 0)])
        min_cost = defaultdict(lambda: math.inf)
        min_cost[src] = 0
        stops = 0
        
        while q and stops <= k:
            for i in range(len(q)):
                stop, cost = q.popleft()

                for neighbor, price in adj[stop]:
                    new_cost = cost + price
                    if new_cost < min_cost[neighbor]:
                        min_cost[neighbor] = new_cost
                        q.append((neighbor, new_cost))
            stops += 1

        return  min_cost[dst] if min_cost[dst] != math.inf else -1
