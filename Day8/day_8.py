from dataclasses import dataclass
import numpy as np
from math import gcd


def readLines(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines


def leastCommonMultiple(values):
    ret = 1
    for x in values:
        ret = (x * ret) // gcd(x,ret)
    return ret


@dataclass
class Node:
    node: str
    left: int
    right: int


class Tree:
    def __init__(self, node_list: list[Node], current_node: Node, commands: str):
        self.node_list = np.array(node_list)
        self.current_node = current_node
        self.commands = commands

    def go_right(self):
        right_node = self.node_list[self.current_node.right]
        self.current_node = right_node
    
    def go_left(self):
        left_node = self.node_list[self.current_node.left]
        self.current_node = left_node

    def find_goal(self):  # finds ZZZ
        counter = 0
        for command in self.commands:
            counter += 1
            if command == 'R':
                self.go_right()
            if command == 'L':
                self.go_left()
        return counter


if __name__ == "__main__":
    lines = readLines("input.txt")
    commands = lines[0].split()[0]
    node_list = []
    id_list = [node.split()[0] for node in lines[2:]]

    for line in lines[2:]:
        node_str = line.split()
        left_str = node_str[2].split("(")[1].split(",")[0]
        right_str = node_str[3].split(")")[0]
        node_list.append(Node(node_str[0], id_list.index(left_str), id_list.index(right_str)))
    
    node_tree = Tree(node_list, node_list[id_list.index('AAA')], commands)
    res = 0
    while (node_tree.current_node.node != 'ZZZ'):
        res += node_tree.find_goal()
    print(f"part1: {res}")

    node_tree_list = []
    n_starting_node_counter = 0
    for i, val in enumerate(id_list):
        if val.endswith('A'):
            node_tree_list.append(Tree(node_list, node_list[i], commands))
            n_starting_node_counter += 1
    common_multiple_dict = {}
    res_list = [0] * n_starting_node_counter
    # while (not all(tree.current_node.node.endswith('Z') for tree in node_tree_list)): This would be brute force. Works but would take ~ 3 hours
    finished = False
    while (True):
        for i, tree in enumerate(node_tree_list):
            res_list[i] += tree.find_goal()
            if tree.current_node.node.endswith('Z'):
                common_multiple_dict[i] = res_list[i] if i not in common_multiple_dict else common_multiple_dict[i]
                if len(common_multiple_dict) == n_starting_node_counter:  # All nodes have found a solution, now we do least common multiple of those values
                    finished = True
        if finished:
            break
    
    print(f"part2: {leastCommonMultiple(common_multiple_dict.values())}")
