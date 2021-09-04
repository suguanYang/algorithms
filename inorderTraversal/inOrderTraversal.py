def inOrderTree(root):
    res = []
    
    def iter(node):
        if node == None:
            return

        iter(node.left)
        res.push(node.value)
        iter(node.right)

    iter(root)
    return res

