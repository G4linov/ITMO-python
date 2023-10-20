class Node:
    def __init__(self, value=0, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root
    
    def getMinimalValue(self, node):
        while node.left:
            node = node.left
        return node

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(value, self.root)

    def _add(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value, None, None, node)
            else:
                self._add(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value, None, None, node)
            else:
                self._add(value, node.right)

    def search(self, value):
        if self.root is None:
            return None
        else:
            return self._search(value, self.root)

    def _search(self, val, node):
        if val == node.value:
            return node
        elif (val < node.value and node.left is not None):
            return self._search(val, node.left)
        elif (val > node.value and node.right is not None):
            return self._search(val, node.right)
        else:
            return None

    def removeNode(self, value):
        currentlyNode = self.search(value)
        
        if currentlyNode is None:
            return None
        
        if currentlyNode.left is None and currentlyNode.right is None:
            nodeParent = currentlyNode.parent
            if nodeParent.left == currentlyNode:
                nodeParent.left = None
            else:
                nodeParent.right = None
        elif currentlyNode.left and currentlyNode.right:
            nodeSwitch = self.getMinimalValue(currentlyNode.right)
            value = nodeSwitch.value
            self.removeNode(self, nodeSwitch.value)
            currentlyNode.value = value
        else:
            if currentlyNode.left:
                child = currentlyNode.left
            else:
                child = currentlyNode.right

            parent = currentlyNode.parent
            
            if currentlyNode != self.root:
                if currentlyNode == parent.left:
                    parent.left = child
                else:
                    parent.right = child
            else:
                self.root = child

    def removeTree(self):
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.left)
            print(str(node.value) + ' ')
            self._printTree(node.right)

tree = Tree()

while(True):
    data_raw = input("Pleace enter value: ")

    if(data_raw == "add"):
        value = input("Pleace enter value for insert into tree: ")
        value = int(value)
        Tree.add(tree, value)

    if(data_raw == "remove node"):
        value = input("Pleace value for delete from tree: ")
        value = int(value)
        Tree.removeNode(tree, value)

    if(data_raw == "remove tree"):
        Tree.removeTree(tree)

    if(data_raw == "search"):
        value = input("Pleace value for searche from tree: ")
        value = int(value)
        FindedNode = Tree.search(tree, value)
        if FindedNode is None:
            print("There is no node in Tree with this value: ", value)
        else:
            print(FindedNode.value, FindedNode.left, FindedNode.right, FindedNode.parent)

    if(data_raw == "print"):
        Tree.printTree(tree)

