# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    ## The Leetcode Function
    def getDecimalValue(self, head: ListNode) -> int:
        binary_string = ""
        itr = head  # Start iterating from the head
        while itr:
            binary_string += str(itr.val)
            itr = itr.next
        return int(binary_string, 2)

# Function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Main function to test the solution
def main():
    solution = Solution()

    # Test case 1: Binary "101" -> Decimal 5
    head = create_linked_list([1, 0, 1])
    print(solution.getDecimalValue(head))  # Output: 5

    # Test case 2: Binary "111" -> Decimal 7
    head = create_linked_list([1, 1, 1])
    print(solution.getDecimalValue(head))  # Output: 7

    # Test case 3: Binary "0" -> Decimal 0
    head = create_linked_list([0])
    print(solution.getDecimalValue(head))  # Output: 0

    # Test case 4: Binary "1001" -> Decimal 9
    head = create_linked_list([1, 0, 0, 1])
    print(solution.getDecimalValue(head))  # Output: 9

    # Test case 5: Binary "1" -> Decimal 1
    head = create_linked_list([1])
    print(solution.getDecimalValue(head))  # Output: 1

if __name__ == "__main__":
    main()
