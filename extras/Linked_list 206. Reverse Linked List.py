class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        next_node = None
        
        while head:
            new_node = ListNode(head.val) # add current value to new node 
            new_node.next = next_node     # link the next node , initially None
            next_node = new_node          # newly created new node become next node for future nodes
            head = head.next              # move up the original LL
            
        return new_node


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

# Helper function to print a linked list
def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(" -> ".join(map(str, result)))

# Main function to test the solution
def main():
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    values = [1, 2, 3, 4, 5]
    head = create_linked_list(values)
    print("Original linked list:")
    print_linked_list(head)

    # Reverse the linked list
    solution = Solution()
    reversed_head = solution.reverseList(head)
    
    # Print the reversed linked list
    print("Reversed linked list:")
    print_linked_list(reversed_head)

if __name__ == "__main__":
    main()
