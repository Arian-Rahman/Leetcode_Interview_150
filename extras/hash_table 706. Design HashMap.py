class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        We'll use an array of fixed size (10^6 + 1) to store key-value pairs.
        Since 0 <= key <= 10^6, this array can directly map keys to values.
        """
        self.size = 10**6 + 1
        self.map = [-1] * self.size  # Initialize all values to -1 (indicating no mapping)

    def put(self, key: int, value: int) -> None:
        """
        Add a key-value pair to the map. If the key already exists, update the value.
        """
        self.map[key] = value

    def get(self, key: int) -> int:
        """
        Retrieve the value associated with the key. Return -1 if the key doesn't exist.
        """
        return self.map[key]  # Returns -1 if the key hasn't been mapped yet

    def remove(self, key: int) -> None:
        """
        Remove the key-value pair from the map. (To be implemented by you)
        """
        self.map[key] = -1

# Example usage
if __name__ == "__main__":
    obj = MyHashMap()
    obj.put(1, 10)  # Put key=1, value=10
    obj.put(2, 20)  # Put key=2, value=20
    print(obj.get(1))  # Output: 10 (key=1 exists in the map)
    print(obj.get(3))  # Output: -1 (key=3 does not exist in the map)
    obj.put(2, 30)  # Update key=2 to value=30
    print(obj.get(2))  # Output: 30 (key=2 has been updated)
    obj.remove(1)  # Implement this!
