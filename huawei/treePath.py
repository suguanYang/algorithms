class Solution:
    def binaryTreePaths(self, root):
        paths = []

        def iter(r, path):
            if r.left != None:
                iter(r.left, path + '->')
            elif r.right != None:
                iter(r.left, path + '->')
            else:
                paths.append(path + r.val)
        
        iter(root, '')
        return paths
