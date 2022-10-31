# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:   #if there is no root we are returning empty list
            return []

        result = []  #to store the result we are creating an empty list

        q = deque()  #bfs has to be done using queue
        q.append(root)  #to start the while loop we are appending the reference of the root in the queue
        
        while q:  #if the queue is empty the loop will break
            size = len(q)  #size parameter
            temp = []  #templist to append the level order values

            for i in range(size):  #iterating through each level
                node = q.popleft()  #we are poping and storing the first element that is in queue 
                temp.append(node.val)  #we are appending its value in the temp list
                if node.left:  #if the node has left element we are appending the referene of the node in the queue
                    q.append(node.left)
                if node.right:  ##if the node has right element we are appending the referene of the node in the queue
                    q.append(node.right)

            result.append(temp)  #we are appending the temp list into the resultant list

        return result  #we are returning the list

         
                    
        