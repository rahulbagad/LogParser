import unittest

from src.constant import INFO, WARNING, LOG_MSG, ERROR
from src.log import what_went_wrong
from src.message import Message


class TestWhatWentWrong(unittest.TestCase):

    def test_what_went_wrong(self):
        message_1 = Message(category=LOG_MSG, message="msg 1", message_type=ERROR.format(err_code=100), time_stamp=100)
        message_2 = Message(category=LOG_MSG, message="msg 2", message_type=ERROR.format(err_code=60), time_stamp=20)
        message_3 = Message(category=LOG_MSG, message="msg 3", message_type=ERROR.format(err_code=70), time_stamp=50)
        message_4 = Message(category=LOG_MSG, message="msg 4", message_type=ERROR.format(err_code=17), time_stamp=18)
        message_5 = Message(category=LOG_MSG, message="msg 5", message_type=INFO, time_stamp=50)
        message_6 = Message(category=LOG_MSG, message="msg 6", message_type=WARNING, time_stamp=30)
        log_messages = [message_1, message_2, message_3, message_4, message_5, message_6]

        error_messages = what_went_wrong(messages=log_messages)

        self.assertEqual(len(error_messages), 3)
        self.assertEqual(error_messages[0], "msg 2")
        self.assertEqual(error_messages[1], "msg 3")
        self.assertEqual(error_messages[2], "msg 1")
