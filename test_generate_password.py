import string
import unittest

from generate_password import build_password


class BuildPasswordTests(unittest.TestCase):
    def test_rejects_non_positive_length(self):
        with self.assertRaises(ValueError):
            build_password(0, True, True, False, False)

    def test_rejects_when_no_character_type_selected(self):
        with self.assertRaises(ValueError):
            build_password(8, False, False, False, False)

    def test_rejects_when_length_shorter_than_required_types(self):
        with self.assertRaises(ValueError):
            build_password(2, True, True, True, False)

    def test_generates_password_with_required_character_types(self):
        password = build_password(12, True, True, True, True)
        self.assertEqual(len(password), 12)
        self.assertTrue(any(ch in string.ascii_uppercase for ch in password))
        self.assertTrue(any(ch in string.ascii_lowercase for ch in password))
        self.assertTrue(any(ch in string.digits for ch in password))
        self.assertTrue(any(ch in string.punctuation for ch in password))


if __name__ == "__main__":
    unittest.main()
