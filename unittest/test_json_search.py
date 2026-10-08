import unittest
from recursive_json_search import *
from test_data import *


class json_search_test(unittest.TestCase):
    '''test module to test search function in
    `recursive_json_search.py`'''

    def test_search_found(self):
        '''key should be found, return list should not be empty'''
        self.assertTrue([] != json_search(key1, data))

    def test_search_not_found(self):
        '''key should not be found, should return an empty list'''
        self.assertTrue([] == json_search(key2, data))

    def test_is_a_list(self):
        '''Should return a list'''
        self.assertIsInstance(json_search(key1, data), list)

    def test_search_nested_dict(self):
        """key nằm trong dictionary lồng nhau"""
        test_data = {
            "user": {
                "profile": {
                    "name": "Alice"
                }
            }
        }

        result = json_search("name", test_data)
        self.assertEqual([{"name": "Alice"}], result)

    def test_search_in_list(self):
        """key nằm trong list chứa dictionary"""
        test_data = {
            "users": [
                {"name": "Alice"},
                {"name": "Bob"}
            ]
        }

        result = json_search("name", test_data)
        self.assertEqual(
            [{"name": "Alice"}, {"name": "Bob"}],
            result
        )

    def test_search_multiple_results(self):
        """key xuất hiện nhiều lần"""
        test_data = {
            "issue1": {
                "issueSummary": "Bug 1"
            },
            "issue2": {
                "issueSummary": "Bug 2"
            }
        }
if __name__ == '__main__':
    unittest.main()