class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_set = [-1] * 1000000
        

    def add(self, key: int) -> None:
        self.hash_set[key] = key
        

    def remove(self, key: int) -> None:
        self.hash_set[key] = -1
        

    def contains(self, key: int) -> bool:
        
        exists = self.hash_set[key]
        return True if exists != -1 else False
        """
        Returns true if this set contains the specified element
        """
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)