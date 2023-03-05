# python3

import sys
import threading

class Node:
    def __init__(self, index):
        self.index = index
        self.children = []

def compute_height(nodes):
    root = None
    for node in nodes:
        if node.parent == -1:
            root = node
        else:
            nodes[node.parent].children.append(node)

    height = 0
    queue = [root]
    while queue:
        height += 1
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.pop(0)
            for child in node.children:
                queue.append(child)
    return height

def main():
    # implement input form keyboard and from files
    input_type = input("Enter (I) or (F): ").lower()

    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    if input_type == 'f':
        while True:
            filename = input("Enter file name (without the letter 'a'): ")
            if 'a' not in filename:
                break
            print("File name cannot contain the letter 'a'!")
        try:
            with open("folder/" + filename) as f:
                n = int(f.readline())
                parent_indices = list(map(int, f.readline().split()))
        except FileNotFoundError:
            print("File not found!")
            return
    # input number of elements
    # input values in one variable, separate with space, split these values
    # call the function and output it's result
    else:
        n = int(input())
        parent_indices = list(map(int, input().split()))

    # Create nodes
    nodes = []
    for i in range(n):
        nodes.append(Node(i))
        nodes[i].parent = parent_indices[i]

    # Compute and print height of tree
    print(compute_height(nodes))

if __name__ == '__main__':
    # In Python, the default limit on recursion depth is rather low,
    # so raise it here for this problem. Note that to take advantage
    # of bigger stack, we have to launch the computation in a new thread.
    sys.setrecursionlimit(10**7)  # max depth of recursion
    threading.stack_size(2**27)   # new thread will get stack of such size
    threading.Thread(target=main).start()
    main()
