import unittest
from setup_names import detail_names

class TestDetailNames(unittest.TestCase):
    def setUp(self):
        # Сетап
        self.d_nam = detail_names

    def test_len(self):
        # Список деталей больше ноля
        self.assertTrue(len(self.d_nam)>0)

    def test_names(self):
        # В каждой детали есть ключи
        for detail in self.d_nam:
            self.assertNotEqual(detail.get("name"), None)
            self.assertNotEqual(detail.get("name_ua"), None)
            self.assertNotEqual(detail.get("description_small"), None)
            self.assertNotEqual(detail.get("description_small_ua"), None)
            self.assertNotEqual(detail.get("keywords"), None)
            self.assertNotEqual(detail.get("keywords_ua"), None)
            self.assertNotEqual(detail.get("portal"), None)
            self.assertNotEqual(detail.get("description_perfect"), None)
            self.assertNotEqual(detail.get("description_good"), None)
            self.assertNotEqual(detail.get("description_fail"), None)
            self.assertNotEqual(detail.get("description_perfect_ua"), None)
            self.assertNotEqual(detail.get("description_good_ua"), None)
            self.assertNotEqual(detail.get("description_fail_ua"), None)
            self.assertNotEqual(detail.get("flaw_perfect"), None)
            self.assertNotEqual(detail.get("flaw_good"), None)
            self.assertNotEqual(detail.get("flaw_fail"), None)
            self.assertNotEqual(detail.get("flaw_perfect_ua"), None)
            self.assertNotEqual(detail.get("flaw_good_ua"), None)
            self.assertNotEqual(detail.get("flaw_fail_ua"), None)

    def test_required_names(self):
        # В каждой детали есть обязательные поля и они заполнены
        for detail in self.d_nam:
            self.assertTrue(len(detail.get("name"))>0)
            self.assertTrue(len(detail.get("name_ua"))>0)
            self.assertTrue(len(detail.get("description_small"))>0)
            self.assertTrue(len(detail.get("description_small_ua"))>0)
            self.assertTrue(len(detail.get("keywords"))>0)
            self.assertTrue(len(detail.get("keywords_ua"))>0)
            self.assertTrue(len(detail.get("portal"))>0)


if __name__ == "__main__":
    unittest.main()
