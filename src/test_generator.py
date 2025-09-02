import unittest
from generator import extract_title

class TestGenerator(unittest.TestCase):
    def test_hash_whitespace(self):
        markdown = ("# Hello World")
        expected_output = "Hello World"
        actual_output = extract_title(markdown)
        self.assertEqual(actual_output, expected_output)
        
