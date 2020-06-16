import sys
from parser import parse
from messages import LogMessage
from typing import List


def parse_log_file(file_path: str, no_of_lines: int) -> List[LogMessage]:
    messages = []
    with open(file_path) as log_file:
        for log_line in [next(log_file) for _ in range(no_of_lines)]:
            messages.append(parse(log_line=log_line))
    log_file.close()
    return messages


args = sys.argv
lines_to_parse = int(args[1])
log_file_path = args[2]
parsed_messages = parse_log_file(file_path=log_file_path, no_of_lines=lines_to_parse)

for msg in parsed_messages:
    print(str(msg))
