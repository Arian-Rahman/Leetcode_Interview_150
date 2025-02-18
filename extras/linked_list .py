class MyHashSet:
    def __init__(self):
        """
        Initialize  data structure .
        We'll use a simple array with a large size (10^6 + 1) to handle integer keys
        since the constraints specify 0 <= key <= 10^6.
        """
        self.size = 10**6 + 1
        self.storage = [False] * self.size  # Use a boolean array to represent presence of keys

    def add(self, key: int) -> None:
        """
        Inserts the value key into the HashSet.
        """
        self.storage[key] = True

    def remove(self, key: int) -> None:
        """
        Removes the value key in the HashSet.
        If the key does not exist, do nothing.
        """
        self.storage[key] = False

    def contains(self, key: int) -> bool:
        """
        Returns True if the HashSet contains the value key, and False otherwise.
        """
        return self.storage[key]

# Main function to test MyHashSet
def main():
    # Create a MyHashSet object
    myHashSet = MyHashSet()

    # Test operations
    myHashSet.add(1)  # Add key 1, set = [1]
    myHashSet.add(2)  # Add key 2, set = [1, 2]
    print(myHashSet.contains(1))  # Returns True (key 1 is in the set)
    print(myHashSet.contains(3))  # Returns False (key 3 is not in the set)
    myHashSet.add(2)  # Add key 2 again, set = [1, 2]
    print(myHashSet.contains(2))  # Returns True (key 2 is in the set)
    myHashSet.remove(2)  # Remove key 2, set = [1]
    print(myHashSet.contains(2))  # Returns False (key 2 is not in the set anymore)

if __name__ == "__main__":
    main()



""" USING LINKED LIST  """


# class Node:
#     def __init__(self, key, next=None):
#         self.key = key
#         self.next = next

# class MyHashSet:
#     def __init__(self):
#         """
#         Initialize  data structure .
#         Use a fixed array of buckets, where each bucket is a linked list.
#         """
#         self.size = 1000  # Number of buckets
#         self.buckets = [None] * self.size  # Array of bucket heads (linked lists)

#     def _hash(self, key):
#         """
#         Hash function to calculate the index for a given key.
#         """
#         return key % self.size

#     def add(self, key: int) -> None:
#         """
#         Insert the key into the HashSet.
#         """
#         index = self._hash(key)
#         if not self.buckets[index]:
#             self.buckets[index] = Node(key)  # Create a new linked list if bucket is empty
#         else:
#             current = self.buckets[index]
#             while current:
#                 if current.key == key:
#                     return  # Key already exists, no need to add
#                 if not current.next:
#                     break  # Reach the end of the list
#                 current = current.next
#             current.next = Node(key)  # Add new node at the end of the linked list

#     def remove(self, key: int) -> None:
#         """
#         Remove the key from the HashSet if it exists.
#         """
#         index = self._hash(key)
#         current = self.buckets[index]
#         prev = None
#         while current:
#             if current.key == key:
#                 if prev:
#                     prev.next = current.next  # Remove current node
#                 else:
#                     self.buckets[index] = current.next  # Remove head node
#                 return
#             prev = current
#             current = current.next

#     def contains(self, key: int) -> bool:
#         """
#         Returns True if the HashSet contains the value key, otherwise False.
#         """
#         index = self._hash(key)
#         current = self.buckets[index]
#         while current:
#             if current.key == key:
#                 return True
#             current = current.next
#         return False

# # Main function to test MyHashSet
# def main():
#     # Create a MyHashSet object
#     myHashSet = MyHashSet()

#     # Test operations
#     myHashSet.add(1)  # Add key 1
#     myHashSet.add(2)  # Add key 2
#     print(myHashSet.contains(1))  # Returns True
#     print(myHashSet.contains(3))  # Returns False
#     myHashSet.add(2)  # Add key 2 again
#     print(myHashSet.contains(2))  # Returns True
#     myHashSet.remove(2)  # Remove key 2
#     print(myHashSet.contains(2))  # Returns False

# if __name__ == "__main__":
#     main()
