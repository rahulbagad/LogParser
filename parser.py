from message import Message
from typing import List, Union

message_code_type_mapping = {'I': 'Info', 'W': 'Warning', 'E': "Error {err_code:d}"}


def parse_message(log_line: str) -> Message:
    tokens = log_line.split(" ")
    return Message(category="Unknown", message=log_line) if is_unknown(tokens) else get_log_message(tokens=tokens)


def is_unknown(tokens: List[str]) -> bool:
    if tokens[0] in ("I", "W") and len(tokens) > 2 and tokens[1].isdigit():
        return False
    if tokens[0] is "E" and len(tokens) > 3 and tokens[1].isdigit() and tokens[2].isdigit():
        return False
    return True


def get_log_message(tokens: List[str]) -> Message:
    message_type = get_message_type(tokens=tokens)
    time_stamp, msg = (int(tokens[2]), " ".join(tokens[3:])) if "Error" in message_type else (
    int(tokens[1]), " ".join(tokens[2:]))
    return Message(category="LogMessage", message_type=message_type, time_stamp=time_stamp, message=msg)


def get_message_type(tokens: List[str]) -> str:
    message_type = message_code_type_mapping[tokens[0]].format(err_code=int(tokens[1]))
    return message_type
