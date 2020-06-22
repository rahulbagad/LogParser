from typing import Optional

from src.constant import LOG_MSG


class Message:
    def __init__(self, category: str, message: str, message_type: Optional[str] = None,
                 time_stamp: Optional[int] = None):
        self.category = category
        self.message_type = message_type
        self.time_stamp = time_stamp
        self.message = message

    def __str__(self):
        if self.category is LOG_MSG:
            return " ".join(
                [self.category, "(" + self.message_type + ")" if "Error" in self.message_type else self.message_type,
                 str(self.time_stamp), self.message])
        else:
            return " ".join([self.category, self.message])
