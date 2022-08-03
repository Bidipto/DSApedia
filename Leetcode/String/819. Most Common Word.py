def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    s = "".join([i.lower() if i.isalnum() else " " for i in paragraph ])
    c = collections.Counter(s.split())
    heap = []
    for val in c:
        heapq.heappush(heap,[-c[val],val])
    banned = set(banned)
    while heap:
        count, val = heapq.heappop(heap)
        if val not in banned:
            return val