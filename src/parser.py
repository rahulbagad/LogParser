from src.constant import UNKNOWN_MSG, INFO, WARNING, LOG_MSG, ERROR
from src.message import Message
from typing import List

message_code_type_mapping = {'I': INFO, 'W': WARNING, 'E': ERROR}


def parse_message(log_line: str) -> Message:
    tokens = log_line.split(" ")
    return Message(category=UNKNOWN_MSG, message=log_line.strip()) if is_unknown(tokens) else get_log_message(tokens=tokens)


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
    return Message(category=LOG_MSG, message_type=message_type, time_stamp=time_stamp, message=msg.strip())


def get_message_type(tokens: List[str]) -> str:
    message_type = message_code_type_mapping[tokens[0]].format(err_code=int(tokens[1]))
    return message_type
