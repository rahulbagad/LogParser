from typing import List
from messages import LogMessage


class Node:
    def __init__(self, log_message: LogMessage):
        self.left = None
        self.right = None
        self.log_message = log_message


class MessageTree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def build_tree(self, log_messages: List[LogMessage]):
        list(map(self.insert, log_messages))

    def insert(self, log_message: LogMessage):
        if self.root:
            self._insert(log_message=log_message, node=self.root)
        else:
            self.root = Node(log_message)

    def _insert(self, log_message: LogMessage, node: Node):
        if log_message.time_stamp < node.log_message.time_stamp:
            if node.left:
                self._insert(log_message=log_message, node=node.left)
            else:
                node.left = Node(log_message=log_message)
        else:
            if node.right:
                self._insert(log_message=log_message, node=node.right)
            else:
                node.right = Node(log_message=log_message)

    def get_in_order_tree_traversal(self) -> List[LogMessage]:
        accumulator = []
        if self.root:
            self._print_tree_in_order(node=self.root, accumulator=accumulator)
        return accumulator

    def _print_tree_in_order(self, node: Node, accumulator: LogMessage):
        if node:
            self._print_tree_in_order(node=node.left, accumulator=accumulator)
            accumulator.append(node.log_message)
            self._print_tree_in_order(node=node.right, accumulator=accumulator)
