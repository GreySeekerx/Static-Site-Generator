import unittest
from generator import extract_title

class TestGenerator(unittest.TestCase):
    def test_hash_whitespace(self):
        markdown = ["# Hello World"]
        expected_output = "Hello World"
        actual_output = extract_title(markdown)
        self.assertEqual(actual_output, expected_output)
        
    def test_alot_of_whitespace(self):
        markdown = ["#    Hello Bob"]
        expected_output = ("Hello Bob")
        actual_output = extract_title(markdown)
        self.assertEqual(actual_output, expected_output)
        
    def test_no_title(self):
        markdown = ["typical text for the markdown"]     
        with self.assertRaises(Exception):
            extract_title(markdown)