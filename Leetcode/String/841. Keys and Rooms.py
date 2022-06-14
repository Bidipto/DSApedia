# 841. Keys and Rooms
# simple dfs with avoiding loops

def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
    seen = set()
    
    def magic(node):
        if node in seen:
            return 
        seen.add(node)
        for nei in rooms[node]:
            if nei not in seen:
                magic(nei)
    