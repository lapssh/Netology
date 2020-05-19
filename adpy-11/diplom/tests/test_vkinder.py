import unittest
from unittest.mock import patch
import main5
from main5 import User
import private_settings
import time


class VKinderTestCase(unittest.TestCase):

    def setUp(self):
        self.user = User
        self.TOKEN = private_settings.TOKEN
        self.api = main5.auth(self.TOKEN)



    def test_groups_get(self):
        lapssh_groups = [179664673, 28229175, 84392011, 73211733, 69741303, 16711345,
                         40839537, 176471180, 37760431, 142410745, 73361137, 11189040]
        lapssh = User('stupport', self.api)
        response = lapssh.groups_get()
        self.assertEqual(response, lapssh_groups)


    def test_info(self):
        info = "{'id': 392307838, 'first_name': 'Алексей', 'last_name': 'Лапшин', 'is_closed': True, 'can_access_closed': True}"
        lapssh = User('stupport', self.api)
        time.sleep(0.33)
        lapssh_info = lapssh.info(self.api)
        self.assertEqual(info, str(lapssh_info))
        print(info)

    def test_get_target(self):
        #time.sleep(0.33)
        with patch('main5.input', return_value='stupport'):
            time.sleep(0.33)
            self.assertEqual(main5.get_target(self.api), 'stupport')
            time.sleep(0.33)
            self.assertNotEqual(main5.get_target(self.api), 'Невиданная дичь')
        #test = main5.get_target(self.api)
        #print(test)

if __name__ == '__main__':
    unittest.main()
