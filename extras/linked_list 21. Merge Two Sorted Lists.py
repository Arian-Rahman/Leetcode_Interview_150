from typing import Optional

# Definition for singly-linked list.
class Solution:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_LL = Solution.ListNode() # the actual LL
        pointer = new_LL  # pointer
        
        while list1 and list2 :
            if list1.val < list2.val :
                pointer.next= list1
                list1=list1.next
            else  :
                pointer.next= list2
                list2=list2.next   
            pointer=pointer.next
                
        if  list1:
            pointer.next= list1
        else :
            pointer.next= list2
            
        # we need to rethrn the actual list(head of the list, skip the dummy one) , not the pointer, which is pointing to the last element 
        return new_LL.next 
 
                           
# Helper function to create a linked list from a list
def create_linked_list(arr):
    """
    Converts a Python list into a linked list.
    Args:
        arr (list): A list of values to create a linked list.
    Returns:
        ListNode: The head of the linked list.
    """
    if not arr:
        return None
    head = Solution.ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Solution.ListNode(value)
        current = current.next
    return head


# Helper function to display the linked list as a Python list
def linked_list_to_list(head):
    """
    Converts a linked list into a Python list.
    Args:
        head (ListNode): The head of the linked list.
    Returns:
        list: A list containing the linked list values.
    """
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# Main function to test the mergeTwoLists implementation
def main():
    # Example inputs
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]

    # Convert the input arrays to linked lists
    l1 = create_linked_list(list1)
    l2 = create_linked_list(list2)

    # Call the mergeTwoLists function (to be implemented by you)
    solution = Solution()
    merged_head = solution.mergeTwoLists(l1, l2)

    # Convert the merged linked list back to a list and print it
    print("Merged Linked List:", linked_list_to_list(merged_head))


if __name__ == "__main__":
    main()
