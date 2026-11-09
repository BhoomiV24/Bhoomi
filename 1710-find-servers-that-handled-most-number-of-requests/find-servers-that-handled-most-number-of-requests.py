
import heapq
class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:

        size = 1
        while size < k:
            size *= 2

        tree = [0] * (2 * size)

        # Initially all servers are available
        for i in range(k):
            tree[size + i] = 1

        for i in range(size - 1, 0, -1):
            tree[i] = tree[2 * i] + tree[2 * i + 1]

        def update(pos, value):
            pos += size
            tree[pos] = value

            pos //= 2
            while pos:
                tree[pos] = tree[2 * pos] + tree[2 * pos + 1]
                pos //= 2

        def find_first(node, left, right, start):
            if right <= start or tree[node] == 0:
                return -1

            if right - left == 1:
                return left

            mid = (left + right) // 2

            res = find_first(node * 2, left, mid, start)

            if res != -1:
                return res

            return find_first(node * 2 + 1, mid, right, start)

        busy = []
        count = [0] * k

        for i in range(len(arrival)):
            time = arrival[i]

            # Release completed servers
            while busy and busy[0][0] <= time:
                finish, server = heapq.heappop(busy)
                update(server, 1)

            # All servers busy
            if tree[1] == 0:
                continue

            preferred = i % k

            # Find available server >= preferred
            server = find_first(1, 0, size, preferred)

            # Wrap around
            if server == -1:
                server = find_first(1, 0, size, 0)

            update(server, 0)

            count[server] += 1

            heapq.heappush(
                busy,
                (time + load[i], server)
            )

        max_count = max(count)

        return [
            i for i in range(k)
            if count[i] == max_count
        ]
        