from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ll_ptr = head 
        new_ll = ListNode()
        new_head = new_ll
        while ll_ptr :
            print(ll_ptr.val)

            if ll_ptr.val != val :
                new_head.next = ll_ptr
                new_head = new_head.next
            ll_ptr=ll_ptr.next 
        
        new_head.next = None # make sure the LL ends properly
        
        return new_ll.next # to skip the dummy head

# Helper function to create a linked list from a list of values
def create_linked_list(arr: List[int]) -> Optional[ListNode]:
    """
    Converts a list of integers into a linked list.
    Args:
        arr (List[int]): List of values to create a linked list.
    Returns:
        ListNode: The head of the created linked list.
    """
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert a linked list to a list of values
def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """
    Converts a linked list into a Python list.
    Args:
        head (ListNode): The head of the linked list.
    Returns:
        List[int]: List of values in the linked list.
    """
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Main function to test the removeElements method
def main():
    # Example input
    values = [7,7,77,7]
    values = [11,3,4,5,6,78,8,89967,5,6]
    val_to_remove =6

    # Create a linked list from the input values
    head = create_linked_list(values)

    # Initialize the solution and call the removeElements method
    solution = Solution()
    new_head = solution.removeElements(head, val_to_remove)

    # Convert the resulting linked list back to a list and print it
    print("Updated Linked List:", linked_list_to_list(new_head))

if __name__ == "__main__":
    main()
