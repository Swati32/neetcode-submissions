class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for source, destination, cost in flights:
            adj[source].append((destination, cost))
        
        q = deque([(src, 0)])
        min_cost = {}
        min_cost[src] = 0
        
        while q and k >= 0:
            for i in range(len(q)):
                stop, cost = q.popleft()

                for neighbor, price in adj[stop]:
                    new_cost = cost + price
                    if neighbor not in min_cost:
                        min_cost[neighbor] = new_cost
                        q.append((neighbor, new_cost))
                    elif min_cost[neighbor] > new_cost:
                        min_cost[neighbor] = new_cost
                        q.append((neighbor, new_cost))
                    
            k -= 1

        return  min_cost[dst] if dst in min_cost else -1
