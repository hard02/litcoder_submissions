class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_sorted_lists(headA, headB):
    dummy = ListNode()
    current = dummy

    while headA is not None or headB is not None:
        if headA is None:
            current.next = ListNode(headB.value)
            headB = headB.next
        elif headB is None:
            current.next = ListNode(headA.value)
            headA = headA.next
        elif headA.value < headB.value:
            current.next = ListNode(headA.value)
            headA = headA.next
        else:
            current.next = ListNode(headB.value)
            headB = headB.next

        current = current.next

    return dummy.next

# Function to print the linked list
def print_linked_list(head):
    current = head
    while current is not None:
        print(current.value)
        current = current.next

# Input
n1 = int(input())
list1 = [int(input()) for _ in range(n1)]

n2 = int(input())
list2 = [int(input()) for _ in range(n2)]

# Create linked lists
headA = ListNode(list1[0])
currentA = headA
for value in list1[1:]:
    currentA.next = ListNode(value)
    currentA = currentA.next

headB = ListNode(list2[0])
currentB = headB
for value in list2[1:]:
    currentB.next = ListNode(value)
    currentB = currentB.next

# Merge and print the result
result_head = merge_sorted_lists(headA, headB)
print_linked_list(result_head)

