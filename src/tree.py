from typing import List

from src.constant import UNKNOWN_MSG
from src.message import Message


class Node:
    def __init__(self, log_message: Message):
        self.left = None
        self.right = None
        self.log_message = log_message


class MessageTree:
    def __init__(self, root: Node):
        self.root = root

    def get_root(self):
        return self.root

    @staticmethod
    def insert(tree: 'MessageTree', log_message: Message):
        tree_root_copy = MessageTree._copy(tree.get_root())
        if log_message.category is UNKNOWN_MSG:
            return tree
        if tree_root_copy:
            MessageTree._insert(log_message=log_message, node=tree_root_copy)
        else:
            tree_root_copy = Node(log_message)
        return MessageTree(tree_root_copy)

    @staticmethod
    def _insert(log_message: Message, node: Node):
        if log_message.time_stamp < node.log_message.time_stamp:
            if node.left:
                MessageTree._insert(log_message=log_message, node=node.left)
            else:
                node.left = Node(log_message=log_message)
        else:
            if node.right:
                MessageTree._insert(log_message=log_message, node=node.right)
            else:
                node.right = Node(log_message=log_message)

    def get_in_order_tree_traversal(self) -> List[Message]:
        accumulator = []
        if self.root:
            self._in_order(node=self.root, accumulator=accumulator)
        return accumulator

    def _in_order(self, node: Node, accumulator: Message):
        if node:
            self._in_order(node=node.left, accumulator=accumulator)
            accumulator.append(node.log_message)
            self._in_order(node=node.right, accumulator=accumulator)

    @staticmethod
    def _copy(root_node: Node):
        if root_node is None:
            return None
        new_node = Node(root_node.log_message)
        new_node.left = MessageTree._copy(root_node.left)
        new_node.right = MessageTree._copy(root_node.right)
        return new_node
