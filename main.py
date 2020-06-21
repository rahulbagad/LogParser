import sys
from parser import parse_message
from messages import LogMessage
from typing import List
from tree import MessageTree


def parse(file_path: str, no_of_lines: int) -> List[LogMessage]:
    messages = []
    with open(file_path) as log_file:
        for log_line in [next(log_file) for _ in range(no_of_lines)]:
            messages.append(parse_message(log_line=log_line))
    log_file.close()
    valid_log_messages = list(filter(lambda x: type(x) is LogMessage, messages))
    return valid_log_messages


def build_tree(log_messages: List[LogMessage]) -> MessageTree:
    tree = MessageTree(None)
    for msg in log_messages:
        tree = tree.insert(tree, msg)
    return tree


def in_order_traversal(tree: MessageTree) -> List[LogMessage]:
    return tree.get_in_order_tree_traversal()


def what_went_wrong(messages: List[LogMessage]) -> List[str]:
    return list(
        filter(lambda x: "Error" in x and int(x.split(" ")[1]) > 50, list(map(lambda x: x.message_type, messages))))


args = sys.argv
lines_to_parse = int(args[1])
log_file_path = args[2]

parsed_messages = parse(file_path=log_file_path, no_of_lines=lines_to_parse)

message_tree = build_tree(log_messages=parsed_messages)

sorted_messages = message_tree.get_in_order_tree_traversal()

what_went_wrong(parsed_messages)
