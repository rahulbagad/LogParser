import sys
from log import parse, build_tree, what_went_wrong

args = sys.argv
lines_to_parse = int(args[1])
log_file_path = args[2]

parsed_messages = parse(file_path=log_file_path, no_of_lines=lines_to_parse)

message_tree = build_tree(log_messages=parsed_messages)

what_went_wrong(parsed_messages)
