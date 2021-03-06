class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
                cur=self.insert(root.left,data)
            if data<=root.data:
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        if not root:
            return -1

        return 1 + max(self.getHeight(root.right), self.getHeight(root.left))


def main():
    T=int(input())
    myTree=Solution()
    root=None
    for i in range(T):
        data=int(input())
        root=myTree.insert(root,data)
    height=myTree.getHeight(root)
    print(height)     

if __name__ == '__main__':
    main()