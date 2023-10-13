#python3 code for sorted insert

class Solution:
    def sortedInsert(self, head1,key):
        # code here
        # return head of edited linked list
        newNode=Node(key)

        
        if newNode.data < head1.data:
             newNode.next=head1
             head1.prev=newNode
             
             return newNode
        
        curr=head1
        nxt=head1.next
        while curr:
            if newNode.data >= curr.data and curr.next == None:
                curr.next=newNode
                newNode.prev=curr
                return head1
                
            if newNode.data >= curr.data and newNode.data < curr.next.data:
                newNode.next=curr.next
                curr.next=newNode
                newNode.prev=curr
                return head1
            
            curr=curr.next
        return head1

