import sys
from src.log import parse, build_tree, what_went_wrong, in_order_traversal

args = sys.argv
lines_to_parse = int(args[1])
log_file_path = args[2]

parsed_messages = parse(file_path=log_file_path, no_of_lines=lines_to_parse)
print("-----------Parsed Messages---------------")
for msg in parsed_messages:
    print(msg)
print("-----------------------------------------\n")

print("-----------Build MessageTree---------------")
message_tree = build_tree(log_messages=parsed_messages)
print("-----------------------------------------\n")

print("-----------Sorted Messages---------------")
sorted_msg = in_order_traversal(message_tree)
for msg in sorted_msg:
    print(msg)
print("-----------------------------------------\n")


print("-----------What Went Wrong---------------")
errors = what_went_wrong(parsed_messages)
for msg in errors:
    print(msg)
print("-----------------------------------------\n")