# 2392. Build a Matrix With Conditions

def buildMatrix(self, k: int, row: List[List[int]], col: List[List[int]]) -> List[List[int]]:
    def topo(nums):
        adj = {i:set() for i in range(k)}
    
        for num, pre in nums:
            adj[num-1].add(pre-1)

        visited = set()
        cycle = set()
        res = list()

        def magic(u):
            if u in visited:
                return True

            if u in cycle:
                return False

            cycle.add(u)

            for v in adj[u]:
                if not magic(v):
                    return False

            cycle.remove(u)
            visited.add(u)
            res.append(u)

            return True

        for i in range(k):
            if not magic(i):
                return []

        return res[::-1]
    
    arr1 = topo(row)
    arr2 = topo(col)
    if not arr1 or not arr2: return []
    print(arr1, arr2)
    res = [[0 for i in range(k)] for i in range(k)]
    for i in range(k):
        res[arr1.index(i)][arr2.index(i)] = i + 1

    return res
    