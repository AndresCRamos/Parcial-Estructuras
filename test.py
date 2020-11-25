from point_1v1 import Tree
from point_1v2 import Tree2

if __name__ == "__main__":
    test = 10
    for i in range(1, test):
        level = 2
        balls = i
        print(f"\t level: {level}\n\t balls:{balls}")
        tree1 = Tree(level)
        tree2 = Tree2(level)
        for j in range(balls-1):
            print(f"Tree 1 Test #{i+1}: {tree1.start()}")
        res1 = tree1.start()
        print(f"\t Tree 1 Test #{i+1}: {res1}")
        print("-----------------------------------------------------------")
        for j in range(balls-1):
            print(f"Tree 2 Test #{i+1}: {tree2.start()}")
        res2 = tree2.start()
        print(f"\t Tree 2 Test #{i+1}: {res2}")
        print(res1 == res2)
        print("\n\n")
