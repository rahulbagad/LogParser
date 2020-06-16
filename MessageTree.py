from messages import LogMessage
from parser import parse


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

    def add(self, log_message: LogMessage):
        if self.root:
            self._add(log_message=log_message, node=self.root)
        else:
            self.root = Node(log_message)

    def _add(self, log_message: LogMessage, node: Node):
        if log_message.time_stamp < node.log_message.time_stamp:
            if node.left:
                self._add(log_message=log_message, node=node.left)
            else:
                node.left = Node(log_message=log_message)
        else:
            if node.right:
                self._add(log_message=log_message, node=node.right)
            else:
                node.right = Node(log_message=log_message)

    def get_in_order_tree(self):
        if self.root:
            self._print_tree_in_order(node=self.root)

    def _print_tree_in_order(self, node: Node):
        if node:
            self._print_tree_in_order(node=node.left)
            print(str(node.log_message) + ' ')
            self._print_tree_in_order(node=node.right)


tree = MessageTree()
tree.add(parse("I 6 Completed armadillo processing"))
tree.add(parse("I 1 Nothing to report"))
tree.add(parse("I 19 I self-destruct sequence"))
tree.add(parse("I 11 Initiating self-destruct sequence"))
tree.add(parse("E 10 12 Initiating self-destruct sequence"))
tree.get_in_order_tree()
