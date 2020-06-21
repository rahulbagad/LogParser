from typing import List

from messages import LogMessage


class Node:
    def __init__(self, log_message: LogMessage):
        self.left = None
        self.right = None
        self.log_message = log_message


class MessageTree:
    def __init__(self, root: Node):
        self.root = root

    def get_root(self):
        return self.root

    def insert(self, tree: 'MessageTree', log_message: LogMessage):
        tree_root_copy = self._copy(tree.get_root())
        if tree_root_copy:
            self._insert(log_message=log_message, node=tree_root_copy)
        else:
            tree_root_copy = Node(log_message)
        return MessageTree(tree_root_copy)

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
            self._in_order(node=self.root, accumulator=accumulator)
        return accumulator

    def _in_order(self, node: Node, accumulator: LogMessage):
        if node:
            self._in_order(node=node.left, accumulator=accumulator)
            accumulator.append(node.log_message)
            self._in_order(node=node.right, accumulator=accumulator)

    def _copy(self, root_node: Node):
        if root_node is None:
            return None
        new_node = Node(root_node.log_message)
        new_node.left = self._copy(root_node.left)
        new_node.right = self._copy(root_node.right)
        return new_node
