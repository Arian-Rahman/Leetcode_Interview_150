from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and not head.next : 
            return head 
        
        ll_ptr = head
        temp_head = ll_ptr
        while ll_ptr and ll_ptr.next:
            next_one = ll_ptr.next
            if ll_ptr.val == next_one.val:  # note this needs to compare value, not nodes themselves
                ll_ptr.next = ll_ptr.next.next
            else : 
                ll_ptr = ll_ptr.next
                
        return temp_head

# Helper function to create a linked list from a list
def create_linked_list(values):
    """
    Converts a list of values into a linked list.
    Args:
        values (list): A list of integers.
    Returns:
        ListNode: The head of the linked list.
    """
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a linked list to a Python list
def linked_list_to_list(head):
    """
    Converts a linked list back to a Python list.
    Args:
        head (ListNode): The head of the linked list.
    Returns:
        list: A list of integers.
    """
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Main function to test the deleteDuplicates function
def main():
    # Example inputs
    list1 = [1, 1, 2, 3, 3,3]

    # Create a linked list from the input list
    head = create_linked_list(list1)

    # Call the deleteDuplicates function
    solution = Solution()
    new_head = solution.deleteDuplicates(head)

    # Convert the resulting linked list back to a list and print it
    print("Resulting Linked List:", linked_list_to_list(new_head))

if __name__ == "__main__":
    main()
