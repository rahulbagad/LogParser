import unittest

from src.constant import UNKNOWN_MSG, INFO, WARNING, LOG_MSG, ERROR
from src.message import Message
from src.log import build_tree, in_order_traversal
from src.tree import MessageTree


class TestBuildTree(unittest.TestCase):
    def test_insert_node(self):
        old_tree = MessageTree(None)
        log_message = Message(category=LOG_MSG, message="Test", message_type=INFO,
                              time_stamp=1000)
        new_tree = MessageTree.insert(tree=old_tree, log_message=log_message)

        self.assertNotEqual(id(old_tree), id(new_tree))
        self.assertEqual(str(new_tree.get_root().log_message), "LogMessage Info 1000 Test")

    def test_insert_unknown(self):
        unknown_msg = Message(category=UNKNOWN_MSG, message="Something else")
        old_tree = MessageTree(None)

        new_tree = old_tree.insert(tree=old_tree, log_message=unknown_msg)

        self.assertEqual(new_tree.get_root(), None)

    def test_build_tree(self):
        message_1 = Message(category=LOG_MSG, message="msg 1", message_type=INFO, time_stamp=100)
        message_2 = Message(category=LOG_MSG, message="msg 2", message_type=ERROR.format(err_code=20), time_stamp=20)
        message_3 = Message(category=LOG_MSG, message="msg 3", message_type=WARNING, time_stamp=50)
        messages = [message_1, message_2, message_3]

        tree = build_tree(log_messages=messages)

        tree_root = tree.get_root()
        self.assertEqual(tree_root.log_message, message_1)
        self.assertEqual(tree_root.left.log_message, message_2)
        self.assertEqual(tree_root.left.right.log_message, message_3)

    def test_in_order(self):
        message_1 = Message(category=LOG_MSG, message="msg 1", message_type=INFO, time_stamp=100)
        message_2 = Message(category=LOG_MSG, message="msg 2", message_type=ERROR.format(err_code=20), time_stamp=20)
        message_3 = Message(category=LOG_MSG, message="msg 3", message_type=WARNING, time_stamp=50)
        messages = [message_1, message_2, message_3]
        tree = build_tree(log_messages=messages)

        sorted_messages = in_order_traversal(tree=tree)

        self.assertEqual(len(sorted_messages), 3)
        self.assertEqual(sorted_messages[0].time_stamp, 20)
        self.assertEqual(sorted_messages[1].time_stamp, 50)
        self.assertEqual(sorted_messages[2].time_stamp, 100)




