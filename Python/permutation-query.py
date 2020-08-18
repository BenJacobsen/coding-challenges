#first naive solution
class Node:
    def __init__ (self, value, next = None):
        self.val = value
        self.next = next

def nodePop(head, val: int):
    if head == None:
        return None
    if head.val == val:
        return head.next
    else:
        head.next = nodePop(head.next, val)
        return head
class Solution:
        
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        ret = []
        head = Node(m, None)
        for x in range(1, m):
            head = Node(m-x, head)
            
        for q in queries:
            posCount = 0
            curr = head
            while curr.val != q:
                posCount += 1
                curr = curr.next
            ret.append(posCount)
            head = nodePop(head, q)
            head = Node(q, head)
        return ret