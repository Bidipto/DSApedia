class MyHashSet:
    def __init__(self):
        self.hash = [[] for i in range(255)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.bucket.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.bucket.remove(key)

    def contains(self, key: int) -> bool:
        self.bucket = self.hash[key%255]
        return key in self.bucket 