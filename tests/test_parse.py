import unittest
from log import parse


class TestParse(unittest.TestCase):

    def test_parse_log_file(self):
        messages = parse("test-sample.log", 10)
        assert len(messages) == 10

        log_messages = self._get_by_category(messages, "LogMessage")
        self.assertEqual(len(log_messages), 9)

        unknown_messages = self._get_by_category(messages, "Unknown")
        self.assertEqual(len(unknown_messages), 1)

    @staticmethod
    def _get_by_category(messages, category):
        return list(filter(lambda x: x.category is category, messages))
