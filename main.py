import sys
from typing import List
from src.log import parse, build_tree, what_went_wrong, in_order_traversal
from src.message import Message


def print_messages(messages: List[Message]):
    for msg in messages:
        print(msg)


def main():
    args = sys.argv
    lines_to_parse = int(args[1])
    log_file_path = args[2]

    parsed_messages = parse(file_path=log_file_path, no_of_lines=lines_to_parse)
    print("-----------Parsed Messages---------------")
    print_messages(parsed_messages)
    print("-----------------------------------------\n")

    print("-----------Build MessageTree---------------")
    message_tree = build_tree(log_messages=parsed_messages)
    print("-----------------------------------------\n")

    print("-----------Sorted Messages---------------")
    sorted_msg = in_order_traversal(message_tree)
    print_messages(sorted_msg)
    print("-----------------------------------------\n")

    print("-----------What Went Wrong---------------")
    errors = what_went_wrong(parsed_messages)
    print_messages(errors)
    print("-----------------------------------------\n")


if __name__ == '__main__':
    main()
