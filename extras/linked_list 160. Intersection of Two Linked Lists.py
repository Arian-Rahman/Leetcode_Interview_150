from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB
        while l1 != l2:
            # Redirect to the other pointer when done, will meet eventually 
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA

        return l1

# Helper function to create a linked list from a list of values
def create_linked_list(arr):
    """
    Converts a list into a linked list.
    Args:
        arr (list): List of values to be converted into a linked list.
    Returns:
        ListNode: The head of the linked list.
    """
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to display the linked list
def display_linked_list(head):
    """
    Converts a linked list to a Python list for easy viewing.
    Args:
        head (ListNode): The head of the linked list.
    Returns:
        list: A list representation of the linked list.
    """
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Helper function to attach two linked lists at a given node
def attach_lists_at_node(headA, headB, intersection_node):
    """
    Attaches two linked lists at a given intersection node.
    Args:
        headA (ListNode): The head of the first linked list.
        headB (ListNode): The head of the second linked list.
        intersection_node (ListNode): The node at which the two linked lists should intersect.
    """
    if not intersection_node:
        return
    currentA = headA
    while currentA.next:
        currentA = currentA.next
    currentA.next = intersection_node
    
    currentB = headB
    while currentB.next:
        currentB = currentB.next
    currentB.next = intersection_node

# Main function to test the getIntersectionNode function
def main():
    # Create two separate linked lists
    listA = [4, 1]
    listB = [5, 6, 1]
    intersection_list = [8, 4, 5]

    # Convert them to linked lists
    headA = create_linked_list(listA)
    headB = create_linked_list(listB)
    intersection_head = create_linked_list(intersection_list)

    # Attach the linked lists at the intersection
    attach_lists_at_node(headA, headB, intersection_head)

    # Display the linked lists
    print("Linked List A:", display_linked_list(headA))
    print("Linked List B:", display_linked_list(headB))

    # Call the method and print the result
    solution = Solution()
    intersection_node = solution.getIntersectionNode(headA, headB)
    if intersection_node:
        print("Intersection Node Value:", intersection_node.val)
    else:
        print("No Intersection")

if __name__ == "__main__":
    main()
