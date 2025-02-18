from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next : return False
        slow = head
        fast = head.next
        # if there's no cicle, one of these will be None and loop breaks , returns false
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast : return True
    
        return False

# Helper function to create a linked list from a list
def create_linked_list_with_cycle(arr, pos):
    """
    Creates a linked list from a Python list and introduces a cycle if pos != -1.
    Args:
        arr (list): The list of values for the linked list.
        pos (int): The position (0-indexed) where the cycle starts. -1 means no cycle.
    Returns:
        ListNode: The head of the linked list.
    """
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head
    nodes = [head]  # To keep track of all nodes for creating the cycle

    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
        nodes.append(current)

    if pos != -1:
        current.next = nodes[pos]  # Create a cycle

    return head

# Helper function to display a linked list (for testing purposes, no cycle)
def display_linked_list(head):
    """
    Prints the linked list values. Stops if a cycle is detected.
    Args:
        head (ListNode): The head of the linked list.
    """
    visited = set()
    result = []
    while head:
        if head in visited:  # Detect a cycle
            result.append("Cycle detected")
            break
        result.append(head.val)
        visited.add(head)
        head = head.next
    print("Linked List:", result)

# Main function to test the `hasCycle` function
def main():
    # Example 1: Linked list without a cycle
    list1 = [3, 2, 0, -4]
    pos1 = -1  # No cycle
    head1 = create_linked_list_with_cycle(list1, pos1)

    # Example 2: Linked list with a cycle
    list2 = [3, 2, 0, -4]
    pos2 = 1  # Cycle starts at index 1 (value 2)
    head2 = create_linked_list_with_cycle(list2, pos2)

    solution = Solution()

    # Test hasCycle for the first linked list
    print("Has Cycle (List 1):", solution.hasCycle(head1))

    # Test hasCycle for the second linked list
    print("Has Cycle (List 2):", solution.hasCycle(head2))

if __name__ == "__main__":
    main()
