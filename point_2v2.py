class Node:
    def __init__(self,  data):
        self.__data = data
        self.__children = []
        self.__parent = None
        self.counter = 0

    def get_children(self):
        return self.__children

    def new_children(self, node):
        self.__children.append(node)

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
        # Compute the height of each subtree
        l_heights = []
        for child in self.get_children():
            l_heights.append(child.height())

        return l_heights

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
                found_in_child = False
                # Search for the character in the children of the present `node`
                for child in node.get_children():
                    if child.get_data() == char:
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
                    # And then point node to the new child
                    node = new_node
            # Everything finished. Mark it as the end of a word.
            node.word_finished = True
        add(self.root, binary)

    def level_order(self):
        def traverse(root):
            curr = [root]
            order = []
            while curr:
                next_level = []
                for n in curr:
                    print(n.get_data())
                    order.extend(n.get_data())
                    next_level.extend(n.get_children())
                curr = next_level
            #order[5 : 8] = [''.join(order[0 : 3])]
            print(order)
        return traverse(self.root)



if __name__ == "__main__":
    inp = "0000 0011 1100 1111"
    inp2 = "0001 0000 1111 1100"
    binTree = BinaryTree()
    for i in inp.split():
        binTree.insert(i)
    print(binTree.pre_order())
    print(binTree.post_order())
    binTree.level_order()
