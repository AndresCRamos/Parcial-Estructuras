class Node:
    def __init__(self,  data):
        self.__data = data
        self.__right = None
        self.__left = None
        self.__parent = None
        self.counter = 0

    def get_r_children(self):
        return self.__right

    def set_r_children(self, new):
        self.__right = new

    def get_l_children(self):
        return self.__left

    def set_l_children(self, new):
        self.__left = new

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_parent(self):
        return self.__parent

    def set_parent(self, new_parent):
        self.__parent = new_parent

    def is_leaf(self):
        return self.get_r_children() is self.get_l_children() is None

    def n_child(self):
        n = 0
        if self.get_r_children():
            n += 1
        if self.get_l_children():
            n += 1
        return n

    def __str__(self):
        return str(self.get_data())


class BinaryTree:
    def __init__(self):
        self.root = Node("root")

    def empty(self):
        return self.root.n_child() == 0

    def pre_order(self):
        def pre(node, lis):
            if node is not None:
                lis.append(node.get_data())
                pre(node.get_l_children(), lis)
                pre(node.get_r_children(), lis)
            return lis

        return pre(self.root, [])

    def post_order(self):
        def pos(node, lis):
            if node is not None:
                for child in node.get_children():
                    pos(child, lis)
                lis.append(node.get_data())
            return lis
        return pos(self.root, [])

    def insert(self, binary):
        def add(node: Node, word: str, index: int):
            if index > len(word)-1:
                return
            char = word[index]
            print(index)
            print("char:", char)
            # Search for the character in the children of the present `node`
            jmp = 0

            if char == 0:
                if node.get_l_children() is None:
                    new = Node(char)
                    node.set_l_children(new)
                    new.set_parent(node)
                    jmp = new
                else:
                    jmp = node.get_l_children()

            elif char == 1:
                if node.get_r_children() is None:
                    new = Node(char)
                    node.set_r_children(new)
                    new.set_parent(node)
                    jmp = new
                else:
                    jmp = node.get_r_children()
            add(jmp, word, index+1)

        add(self.root, binary, 0)

    def prefix(self):
        def search_prefix(root):
            level_list = []
            h = self.treeHeight()
            for level in range(1, h + 1):
                print("h", level)
                lev = search_prefix_level(root, level, [])
                level_list.append(lev)
            return level_list

        # Print nodes at a given level
        def search_prefix_level(root, level, res):
            if root is None:
                return
            if level == 1:
                res.append(root)
            elif level > 1:
                if len(root.get_children()) == 1 or root.get_data() == "root":
                    for child in root.get_children():
                        search_prefix_level(child, level - 1, res)
                else:
                    res.append(root)
                    return
            return res

        return search_prefix(self.root)



    def level_order(self):
        def print_level_order(root):
            level_list_2 = []
            h = self.treeHeight()
            print(h)
            for level in range(1, h + 1):
                lev = print_a_level(root, level, [])
                level_list_2.append(lev)
            
            res = ""
            for i in range(len(level_list_2)):
                res += f"Level {i}: "
                for j in range(len(level_list_2[i])):
                    res += level_list_2[i][j].get_data()+" "
                res += "\n"

            return res

        # Print nodes at a given level
        def print_a_level(root, level, res):
            if root is None:
                res.append(None)
                return
            if level == 1:
                res.append(root)
            elif level > 1:
                for child in root.get_children():
                    print_a_level(child, level - 1, res)
            return res

        return print_level_order(self.root)

    def treeHeight(self):
        def tree_height_rec(node):
            root = self.root
            # Base Case
            if root is None:
                return 0

            # Create a empty queue for level order traversal
            q = []

            # Enqueue Root and Initialize Height
            q.append(root)
            height = 0

            while (True):

                # nodeCount(queue size) indicates number of nodes
                # at current level
                nodeCount = len(q)
                if nodeCount == 0:
                    return height

                height += 1

                # Dequeue all nodes of current level and Enqueue
                # all nodes of next level
                while (nodeCount > 0):
                    node = q[0]
                    q.pop(0)
                    if node.get_l_children() is not None:
                        q.append(node.get_l_children())
                    if node.get_r_children() is not None:
                        q.append(node.get_r_children())

                    nodeCount -= 1


if __name__ == '__main__':
    tree = BinaryTree()
    tree.insert("0000")
    print(tree.pre_order())
    print(tree.level_order())
