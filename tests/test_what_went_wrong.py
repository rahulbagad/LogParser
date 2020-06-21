import unittest

from log import what_went_wrong
from message import Message


class TestWhatWentWrong(unittest.TestCase):

    def test_what_went_wrong(self):
        message_1 = Message(category="LogMessge", message="msg 1", message_type="Error 100", time_stamp=100)
        message_2 = Message(category="LogMessge", message="msg 2", message_type="Error 60", time_stamp=20)
        message_3 = Message(category="LogMessge", message="msg 3", message_type="Error 70", time_stamp=50)
        message_4 = Message(category="LogMessge", message="msg 3", message_type="Error 17", time_stamp=18)
        message_5 = Message(category="LogMessge", message="msg 3", message_type="Info", time_stamp=50)
        message_6 = Message(category="LogMessge", message="msg 3", message_type="Warning", time_stamp=30)
        log_messages = [message_1, message_2, message_3, message_4, message_5, message_6]

        error_messages = what_went_wrong(messages=log_messages)

        self.assertEqual(len(error_messages), 3)
        self.assertEqual(error_messages[0], "Error 60")
        self.assertEqual(error_messages[1], "Error 70")
        self.assertEqual(error_messages[2], "Error 100")
