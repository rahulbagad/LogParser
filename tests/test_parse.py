import unittest

from constants import UNKNOWN_MSG, LOG_MSG, INFO
from log import parse


class TestParse(unittest.TestCase):

    def test_parse_log_file(self):
        messages = parse("tests/test-sample.log", 10)
        assert len(messages) == 10

        log_messages = self._get_by_category(messages, LOG_MSG)
        self.assertEqual(len(log_messages), 9)
        self.assertEqual(log_messages[0].message_type, INFO)
        self.assertEqual(log_messages[0].time_stamp, 6)
        self.assertEqual(log_messages[0].message, "Completed armadillo processing")

        unknown_messages = self._get_by_category(messages, UNKNOWN_MSG)
        self.assertEqual(len(unknown_messages), 1)
        self.assertEqual(unknown_messages[0].category, UNKNOWN_MSG)

    @staticmethod
    def _get_by_category(messages, category):
        return list(filter(lambda x: x.category is category, messages))
