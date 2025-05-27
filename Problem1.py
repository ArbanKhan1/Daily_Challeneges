#Given a sorted circular linked list, the task is to insert a new node in this circular linked list so that it remains a sorted circular linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def sortedInsert(self, head, data):
        # Case 1: List is empty (head is None)
        if head is None:
            new = Node(data)
            new.next = new  # Circular reference
            return new

        # Case 2: Insert at the beginning (when data is smaller than head)
        if data < head.data:
            new = Node(data)
            new.next = head
            # Find the last node to complete the circle
            temp = head
            while temp.next != head:
                temp = temp.next
            temp.next = new
            return new  # New node becomes the new head
        
        # Case 3: Traverse to find the correct insertion point
        current = head
        while current.next != head:
            # If data fits between current and current.next
            if current.data <= data <= current.next.data:
                new = Node(data)
                new.next = current.next
                current.next = new
                return head
            current = current.next
        
        # Case 4: Insert at the end (when data is larger than all nodes)
        new = Node(data)
        current.next = new
        new.next = head  # Close the circular link
        return head