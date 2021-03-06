from src.parser import parse_message
from src.message import Message
from typing import List
from src.tree import MessageTree


def parse(file_path: str, no_of_lines: int) -> List[Message]:
    messages = []
    with open(file_path) as log_file:
        for log_line in [next(log_file) for _ in range(no_of_lines)]:
            messages.append(parse_message(log_line=log_line))
    log_file.close()
    return messages


def build_tree(log_messages: List[Message]) -> MessageTree:
    tree = MessageTree(None)
    for log_message in log_messages:
        tree = MessageTree.insert(tree, log_message)
    return tree


def in_order_traversal(tree: MessageTree) -> List[Message]:
    return tree.get_in_order_tree_traversal()


def what_went_wrong(messages: List[Message]) -> List[str]:
    tree = build_tree(log_messages=messages)
    sorted_messages = tree.get_in_order_tree_traversal()
    errors = list(filter(lambda x: "Error" in x.message_type and int(x.message_type.split(" ")[1]) > 50, sorted_messages))
    return list(map(lambda x: x.message, errors))