import random
import collections as col


# subtask 1
# Given a binary tree, write a function that returns the sum of the values of that tree.

class Node:
    def __init__(self, l=None, r=None, v=0) -> None:
        self.left = l
        self.right = r
        self.value = v


def get_tree(max=50):
    nodes = [Node(v=random.randint(-100, 100)) for i in range(max + 1)]

    tree = Node()
    for i in range(max):
        sight = random.choice(['l', 'r'])
        val = random.randint(-100, 100)
        vall = random.randint(0, max)
        if sight == 'l':
            tree = Node(l=tree, r=nodes[vall], v=val)
        else:
            tree = Node(l=nodes[vall], r=tree, v=val)
    return tree


tree1 = get_tree(5)
tree2 = get_tree(10)
tree3 = get_tree(50)


def solution1(tree: Node):
    """
    Return maximum integer given list of integers.
    Args:
        tree - tree
    Returns:
        float.
    """
    if tree.left is None and tree.right is None:
        return tree.value
    elif tree.left is None and tree.right is not None:
        return tree.value + solution1(tree.right)
    elif tree.left is not None and tree.right is None:
        return tree.value + solution1(tree.left)
    else:
        return tree.value + solution1(tree.left) + solution1(tree.right)


# subtask 2
# Find an area of the intersection of two rectangles.

class Rect:
    def __init__(self, x=0, y=0, w=0, h=0) -> None:
        self.x = x
        self.y = y
        self.wight = w
        self.height = h


def intersection(a1, b1, a2, b2):
    """
    Returns length of intersection if two segments intersects
    Takes:
        a1 - start of first segment
        b1 - end of first segment
        a2 - start of second segment
        b2 - end of second segment
    """
    first, second = min((a1, b1), (a2, b2)), max((a1, b1), (a2, b2))
    if second[0] >= first[1]:
        return 0
    elif second[0] < first[1] <= second[1]:
        return first[1] - second[0]
    else:
        return second[1] - second[0]


def solution2(r1: Rect, r2: Rect):
    return intersection(r1.x, r1.x + r1.wight, r2.x, r2.x + r2.wight) * \
           intersection(r1.y, r1.y + r1.height, r2.y, r2.y + r2.height)


rects = [Rect(x=random.randint(-100, 100),
              y=random.randint(-100, 100),
              w=random.randint(0, 100),
              h=random.randint(0, 100)) for i in range(20)]

r1 = rects[random.randint(0, 19)]
r2 = rects[random.randint(0, 19)]


# subtask 3
# Write an efficient function that checks whether any permutation of an input string is a palindrome.
# Note that the function is not a palindrome check

def solution3(s: str):
    c = col.Counter(s)
    return sum([1 if n % 2 == 1 else 0 for n in c.values()]) in (0, 1)


def solution(tree: Node, r1: Rect, r2: Rect, s: str):
    return solution1(tree), solution2(r1, r2), solution3(s)


def test_func1():
    print(solution1(tree1))
    print(solution1(tree2))
    print(solution1(tree3))

    print(solution2(r1, r2))

    assert solution3('civic') == True, "Check your implementation!"
    assert solution3('ivicc') == True, "Check your implementation!"
    assert solution3('civil') == False, "Check your implementation!"
    assert solution3('livci') == False, "Check your implementation!"

    print("Local tests for func passed!")


if __name__ == "__main__":
    test_func1()
