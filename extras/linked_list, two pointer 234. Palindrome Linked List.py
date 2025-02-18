# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True  # Empty list or single node is always a palindrome
        
        # find middle node 
        fast=head 
        slow=head
        while fast :
            fast =fast.next.next
            slow = slow.next 
        # now slow points to the mid point 
        
        # store a new LL in reverse order from mid point
        prev = None
        while slow: ## Need to study reversing a LL
            temp_next = slow.next
            slow.next = prev
            prev = slow 
            slow = temp_next
            
        p1,p2 = head,prev
        
        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next          
        
        return True

# Helper functions to test the solution
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def main():
    solution = Solution()
    
    # Test case 1: Palindrome
    head1 = create_linked_list([1, 2, 2, 1])
    print("Is Palindrome?", solution.isPalindrome(head1))  # Output: True
    
    # Test case 2: Not a palindrome
    head2 = create_linked_list([1, 2, 3, 4])
    print("Is Palindrome?", solution.isPalindrome(head2))  # Output: False
    
    # Test case 3: Single node
    head3 = create_linked_list([1])
    print("Is Palindrome?", solution.isPalindrome(head3))  # Output: True

if __name__ == "__main__":
    main()
