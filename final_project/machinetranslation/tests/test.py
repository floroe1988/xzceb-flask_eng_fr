from ibm_cloud_sdk_core import ApiException

from translator import englishToFrench, frenchToEnglish
import unittest


class TestFrenchTranslation(unittest.TestCase):
    def test_frenchToEnglish_assertNotEqual(self):
        self.assertNotEqual(frenchToEnglish("Bonjour"), "")

    def test_frenchToEnglish_assertEqual(self):
        self.assertEqual(frenchToEnglish("Bonjour"), {'character_count': 7,
                                                      'translations': [{'translation': 'Hello'}],
                                                      'word_count': 1})


class TestEnglishTranslation(unittest.TestCase):
    def test_englishToFrench_assertNotEqual(self):
        self.assertNotEqual(frenchToEnglish("Hello"), "")

    def test_englishToFrench_assertEqual(self):
        self.assertEqual(englishToFrench("Hello"), {'character_count': 5,
                                                    'translations': [{'translation': 'Bonjour'}],
                                                    'word_count': 1})


if __name__ == "__main__":
    unittest.main()