import unittest
from main import ModelObj
from setup_names import detail_names
from settings import model

class TestModelObj(unittest.TestCase):
    def setUp(self):
        # Сетап
        self.model_obj = ModelObj(model, detail_names)

    def test_init_valls(self):
        # Инит заполнен
        self.assertTrue(len(self.model_obj.vendor)>0)
        self.assertTrue(len(self.model_obj.model)>0)
        self.assertTrue(len(self.model_obj.keywords_string)>0)
        self.assertTrue(len(self.model_obj.state)>0)
        self.assertTrue(len(self.model_obj.names_dict)>0)
        # Пути
        self.assertTrue(len(self.model_obj.model_dir)>0)
        self.assertTrue(len(self.model_obj.all_photos_dir)>0)

    def test_get_names_list(self):
        # Поля объектов модели заполнены
        names_dict = self.model_obj.get_names_list()
        for detail in names_dict:
            self.assertNotEqual(detail.get('vendor'), None)
            self.assertNotEqual(detail.get('model'), None)
            self.assertNotEqual(detail.get('model_name'), None)
            self.assertNotEqual(detail.get('name'), None)
            self.assertNotEqual(detail.get('name_ua'), None)
            self.assertNotEqual(detail.get('description_small'), None)
            self.assertNotEqual(detail.get('description_small_ua'), None)
            self.assertNotEqual(detail.get('description_perfect'), None)
            self.assertNotEqual(detail.get('description_good'), None)
            self.assertNotEqual(detail.get('description_fail'), None)
            self.assertNotEqual(detail.get("description_perfect_ua"), None)
            self.assertNotEqual(detail.get("description_good_ua"), None)
            self.assertNotEqual(detail.get("description_fail_ua"), None)
            self.assertNotEqual(detail.get("flaw_perfect"), None)
            self.assertNotEqual(detail.get("flaw_good"), None)
            self.assertNotEqual(detail.get("flaw_fail"), None)
            self.assertNotEqual(detail.get("flaw_perfect_ua"), None)
            self.assertNotEqual(detail.get("flaw_good_ua"), None)
            self.assertNotEqual(detail.get("flaw_fail_ua"), None)
            self.assertNotEqual(detail.get('keywords'), None)
            self.assertNotEqual(detail.get('keywords_ua'), None)
            self.assertNotEqual(detail.get('portal'), None)
            self.assertNotEqual(detail.get('dir_path'), None)

if __name__ == "__main__":
    unittest.main()
