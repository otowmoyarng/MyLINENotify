import unittest
from settings import Settings


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
                "token": token_expect,
                "entryPoint": entryPoint_expect
            }
        }
        with open("setting_test.json", 'w') as f:
            json.dump(setting_test, f, indent=4)
        self.instance = Settings("setting_test.json")

    def test_constructor(self):
        self.assertIsNotNone(self.instance)

    def test_property(self):
        self.assertEqual(token_expect, self.instance.Token)
        self.assertEqual(entryPoint_expect, self.instance.EntryPoint)


if __name__ == '__name__':
    unittest.main()
