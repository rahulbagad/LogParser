class LogMessage:
    def __init__(self, message_type: str, time_stamp: int, message: str):
        self.message_type = message_type
        self.time_stamp = time_stamp
        self.message = message

    def __str__(self):
        return " ".join(["LogMessage", self.message_type, str(self.time_stamp), self.message])


class UnknownMessage:
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return " ".join(["Unknown", self.message])
