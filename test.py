import unittest
import pandas as pd 

test_users = {"test_user":{"name": "Test User","favorite_color": "Black"}}
test_user = {"test_user":{"id": "test","name": "Test User","favorite_color": "Black"}}


class Testing (unittest.TestCase):

    def test_users(self):
        data_test = pd.read_json('test_users.json')
        data_test = data_test.to_dict()
        for element in data_test.values():
            if 'id' in element:
                del element['id']
        self.assertEqual(data_test,test_users)

    def test_user(self):
        data_test = pd.read_json('test_users.json')
        data_test = data_test.to_dict()
        username = 'test_user'
        if username in data_test.keys():
            self.assertEqual(data_test,test_user)



if __name__ == '__main__':
    unittest.main()



    