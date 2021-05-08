from settings import Settings
import unittest
import json


class SettingsTest(unittest.TestCase):
    """[summary]
    Setttingsユニットテスト
    Args:
        unittest ([type]): [description]
    """
    instance: Settings
    token_expect = "abcde12345"
    entryPoint_expect = "http://localhost:12345"

    def setUp(self):
        """[summary]
        テスト準備
        """
        setting_test = {
            "LINENotify": {
                "token": self.token_expect,
                "entryPoint": self.entryPoint_expect
            }
        }
        with open("setting_test.json", 'w') as f:
            json.dump(setting_test, f, indent=4)
        self.instance = Settings("setting_test.json")

    def test_constructor(self):
        self.assertIsNotNone(self.instance)

    def test_property(self):
        self.assertEqual(self.token_expect, self.instance.Token)
        self.assertEqual(self.entryPoint_expect, self.instance.EntryPoint)


if __name__ == '__name__':
    unittest.main()
