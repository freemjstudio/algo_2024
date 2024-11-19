"""
https://leetcode.com/problems/course-schedule/description/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. \You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses

"""

from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree_dict = [0] * numCourses # 진입 차수 기록
        # y -> x
        for x, y in prerequisites:
            graph[y].append(x) # 인접 노드 간선 연결 
            indegree_dict[x] += 1

        ### BFS 
        queue = deque([])
        visited = [False] * (numCourses)

        # 진입 차수가 0 인 노드만 queue 에 삽입한다. 
        for node in range(numCourses):
            if indegree_dict[node] == 0: 
                queue.append(node)
                visited[node] = True 

        while queue: 
            x = queue.popleft()
        
            for next_node in graph[x]: # 인접한 노드들을 조회한다. 
                indegree_dict[next_node] -= 1
                if indegree_dict[next_node] == 0 and not visited[next_node]: 
                    queue.append(next_node)
                    visited[next_node] = True 
                    
        for node in range(numCourses):
            if not visited[node]:
                return False 
        return True 