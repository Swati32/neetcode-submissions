class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        in_degree = [0] * numCourses

        for course, req in prerequisites:
            prereqs[req].append(course)
            in_degree[course] += 1

        queue = deque([])
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)
       
        completed = 0
        while queue:
            req = queue.popleft()
            completed += 1

            for neighbor in prereqs[req]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
     
        return completed == numCourses
