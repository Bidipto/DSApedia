# 1828. Queries on Number of Points Inside a Circle

def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        
        for x,y,r in queries:
            t = 0
            for x1,y2 in points:
                ed = math.sqrt(pow(x-x1,2)+pow(y-y2,2))
                if ed<=r:
                    t += 1
            res.append(t)
        
        return res