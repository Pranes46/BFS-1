"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:  #tc - o(n(. sc - o(n)
        
        
        if root==None:  #returning empty list if there is no root/tree
            return []
        
        q = deque() #initializing queue to do BFS
        q.append(root)  #appending root reference in q
        result = []  #initializing an empty list to append the result
        while q:  #the loop will run untill there is no value in queue
            size = len(q)  #we are doing level order traversal so we are calculating len of queue to run the loop
            level = []  #temp list to store the node values in this
            for i in range(size):  #the loop will till the len of queue
                node = q.popleft()  #we are popping out the node from the queue to process its child
                level.append(node.val)  #appendind the node value in level list
                
                for child in node.children:  #this is an n nary tree so we have many children in a list. so to access the children from the list we are using this loop
                    q.append(child)  #appending the children one by one in the queue
                    
                    
            result.append(level)  #appending the level list into the resultant array
            
        return result  #returning result
        
        
