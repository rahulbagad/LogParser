from messages import LogMessage
from parser import parse


class Node:
    def __init__(self, message: LogMessage):
        self.left = None
        self.right = None
        self.message = message


class MessageTree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self, msg: LogMessage):
        if self.root is None:
            self.root = Node(msg)
        else:
            self._add(msg, self.root)

    def _add(self, msg, node):
        if msg.time_stamp < node.message.time_stamp:
            if node.left is not None:
                self._add(msg, node.left)
            else:
                node.left = Node(msg)
        else:
            if node.right is not None:
                self._add(msg, node.right)
            else:
                node.right = Node(msg)

    def print_tree(self):
        if self.root:
            self._print_tree_pre_order(self.root)

    def _print_tree_in_order(self, node):
        if node:
            self._print_tree_in_order(node.left)
            print(str(node.message) + ' ')
            self._print_tree_in_order(node.right)

    def _print_tree_pre_order(self, node):
        if node:
            print(str(node.message) + ' ')
            self._print_tree_pre_order(node.left)
            self._print_tree_pre_order(node.right)

    def _print_tree_post_order(self, node):
        if node:
            self._print_tree_post_order(node.left)
            self._print_tree_post_order(node.right)
            print(str(node.message) + ' ')


tree = MessageTree()
tree.add(parse("I 6 Completed armadillo processing"))
tree.add(parse("I 1 Nothing to report"))
tree.add(parse("I 11 Initiating self-destruct sequence"))
tree.print_tree()