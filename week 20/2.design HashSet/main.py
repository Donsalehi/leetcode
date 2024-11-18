class MyHashSet:

    def __init__(self):
        self.hash = dict()

    def add(self, key: int) -> None:
        self.hash[key] = 0

    def remove(self, key: int) -> None:
        if self.contains(key):
            del self.hash[key]

    def contains(self, key: int) -> bool:
        return key in self.hash


myHashSet = MyHashSet()
print(myHashSet.add(1))
print(myHashSet.add(2))
print(myHashSet.contains(1))
print(myHashSet.contains(3))
print(myHashSet.add(2))
print(myHashSet.contains(2))
print(myHashSet.remove(2))
print(myHashSet.contains(2))
