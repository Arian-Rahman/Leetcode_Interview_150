class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        slow = head
        fast = head
        
        while fast and fast.next:  
            # list stops when fast has no next 
            # need to break out when fast is none else fast.next causes runtime error 
            slow = slow.next      
            fast = fast.next.next 
        
        return slow  # slow is now pointing to the middle node
        

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list from a given node
def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    print(" -> ".join(map(str, result)))

def main():
    # Example 1: Linked list [1, 2, 3, 4, 5]
    values = [1, 2, 3, 4, 5]
    head = create_linked_list(values)
    solution = Solution()
    middle = solution.middleNode(head)
    print("Middle node and onward:")
    print_linked_list(middle)

    # Example 2: Linked list [1, 2, 3, 4, 5, 6]
    values = [1, 2, 3, 4, 5, 6]
    head = create_linked_list(values)
    middle = solution.middleNode(head)
    print("Middle node and onward:")
    print_linked_list(middle)

if __name__ == "__main__":
    main()
