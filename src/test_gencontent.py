import unittest
from gencontent import extract_title


class TestGenContent(unittest.TestCase):
    def test_extract_title(self):
        md = """
This is **bolded** paragraph

## This is a header2
# This is a header1
"""
        title = extract_title(md)
        self.assertEqual(
            title,
            "This is a header1"
        )


    def test_with_extract_title_raises(self):
        md = """
This is **bolded** paragraph

## This is a header2
"""
        with self.assertRaises(Exception):
            title = extract_title(md)

if __name__ == "__main__":
    unittest.main()
