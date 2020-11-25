from operator import methodcaller


class Node:
    def __init__(self,  data):
        self.__data = data
        self.__children = [None]*2
        self.__parent = None
        self.counter = 0

    def get_children(self):
        return self.__children

    def new_children(self, node):
        if node.get_data() == 0:
            self.__children[0] = node
        else:
            self.__children[1] = node

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_parent(self):
        return self.__parent

    def set_parent(self, new_parent):
        self.__parent = new_parent

    def is_leaf(self):
        return len(self.__children) == 0

    def n_child(self):
        return len(self.__children) == 0

    def height(self):
        def rec(node):
            if node is None:
                return 0
            max_depth = 0
            for child in node.get_children():
                max_depth = max(max_depth, rec(child))
            return max_depth + 1

        return rec(self)

    def branch(self):
        def prefix_branch(node, branch):
            if node is None:
                return branch
            else:
                branch.append(node)
                prefix_branch(node.get_parent(), branch)
            return branch

        return prefix_branch(self, [])

    def __str__(self):
        return f"Node: {str(self.get_data())}"


class BinaryTree:
    def __init__(self):
        self.root = Node("root")

    def empty(self):
        return self.root.n_child() == 0

    def pre_order(self):
        def pre(node, lis):
            if node is not None:
                lis.append(node.get_data())
                for child in node.get_children():
                    pre(child, lis)
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
        def add(root, word: str):
            """
            Adding a word in the trie structure
            """
            node = root
            for char in word:
                print("char", char)
                found_in_child = False
                # Search for the character in the children of the present `node`
                for child in node.get_children():
                    if child is not None and child.get_data() == char:
                        # We found it, increase the counter by 1 to keep track that another
                        # word has it as well
                        child.counter += 1
                        # And point the node to the child that contains this char
                        node = child
                        found_in_child = True
                        break
                # We did not find it so add a new child
                if not found_in_child:
                    new_node = Node(char)
                    node.new_children(new_node)
                    new_node.set_parent(node)
                    # And then point node to the new child
                    node = new_node
                    print(new_node)
            # Everything finished. Mark it as the end of a word.
            node.word_finished = True
        add(self.root, binary)

    def prefix(self):
        def search_prefix(root):
            level_list = []
            h = root.height()
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
            level_list = []
            h = root.height()
            for level in range(1, h + 1):
                lev = print_a_level(root, level, [])
                level_list.append(lev)

            res = ""
            for i in range(len(level_list)):
                res += f"Level {i}: "
                for j in range(len(level_list[i])):
                    res += level_list[i][j].get_data()+" "
                res += "\n"

            return res

        # Print nodes at a given level
        def print_a_level(root, level, res):
            if root is None:
                return
            if level == 1:
                res.append(root)
            elif level > 1:
                for child in root.get_children():
                    print_a_level(child, level - 1, res)
            return res

        return print_level_order(self.root)

if __name__ == "__main__":
    inp = "0000 0011 1100 1111"
    inp2 = "0001 0000 1111 1100"
    inp3 = "0101 1010"
    binTree = BinaryTree()
    for i in inp.split():
        #print(i)
        binTree.insert(i)
    print("preorder", binTree.pre_order())
    print("level Order:\n")
    print(binTree.level_order())
    print("prefix: ")
    r = binTree.prefix()
    for i in r:
        print(list(map(methodcaller("__str__"), i)))
    n = r[2]
    N = n[0]
    print()
    print("N", N)
    print(list(map(methodcaller("__str__"), N.branch())))
