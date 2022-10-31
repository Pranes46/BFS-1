# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:  
        
        #Using DFS
        
        self.result = []  #to store the result we are initializing this list
        self.recurr(root,0)  #we are passing the roor and count value as 0
        return self.result  #returning result
        
    def recurr(self,root,c):
        if not root:   #if there is no root we are returning empty list
            return 
        if c>=len(self.result):  #if count is less than length of the results we are appending the node value, the first recurrsion is for right side so the count will increase by 1. If there is no right node, the left node value will append on the list. 
            self.result.append(root.val)
            
        self.recurr(root.right,c+1)  #calling the recurrsion function with the right node
        
        self.recurr(root.left,c+1)   #calling the recurrsion function with the left node
        
        
        
        
        
        
        
        
        