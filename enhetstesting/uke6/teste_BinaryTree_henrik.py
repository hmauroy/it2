from BinaryTreeNode import BinaryTreeNode

rot = BinaryTreeNode("x")
#print(type(rot.level).__name__)
#print(rot.hasRight())


rot.left = BinaryTreeNode("+")
rot.right = BinaryTreeNode("-")


rot.left.left = BinaryTreeNode("a")
rot.left.right = BinaryTreeNode("b")

rot.right.left = BinaryTreeNode("c")
rot.right.right = BinaryTreeNode("d")


print("preOrder")
rot.prefixOrder()
print("--------------")
print("inOrder")
rot.infixOrder()
print("--------------")
print("postOrder")
rot.postfixOrder()
print("--------------")
print("levelOrder")
rot.levelOrder()


from queue import SimpleQueue
FIFOQueue = SimpleQueue()
FIFOQueue.put(rot)
#print(FIFOQueue.get())
