import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        # dist[u][cnt] stores minimum weight to reach node u 
        # with cnt consecutive identical characters ending at u
        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]
        
        # Priority Queue stores tuples of (cost, current_node, consecutive_count)
        # Starting at node 0, the label sequence starts with labels[0] (count = 1)
        pq = [(0, 0, 1)]
        dist[0][1] = 0
        
        while pq:
            d, u, cnt = heapq.heappop(pq)
            
            # If we found a longer path than already recorded for this state, skip
            if d > dist[u][cnt]:
                continue
                
            # If we reached the target node, return the distance
            if u == n - 1:
                return d
                
            for v, w in adj[u]:
                # Determine new consecutive character count
                new_cnt = cnt + 1 if labels[u] == labels[v] else 1
                
                # Only proceed if consecutive count does not exceed k
                if new_cnt <= k and d + w < dist[v][new_cnt]:
                    dist[v][new_cnt] = d + w
                    heapq.heappush(pq, (d + w, v, new_cnt))
                    
        return -1