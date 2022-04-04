# A Program to check if strings are rotations of each other or not
def rotateString(self, s: str, goal: str) -> bool:
        s = list(s)
        goal = list(goal)
        for i in range(len(s)):
            temp = s[0]
            for j in range(len(s)-1):
                s[j] = s[j+1]
            s[-1] = temp
            if s == goal:
                return True
        return False

#also an one liner 
def rotateString(self, s: str, goal: str) -> bool:
    return len(s) == len(goal) and goal in s + s