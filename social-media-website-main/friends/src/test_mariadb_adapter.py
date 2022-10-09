import unittest
import mariadb_adapter as mariadb
import random

class TestMariadbAdapter(unittest.TestCase):
    def test_insert(self):
        user_name = str(random.randint(1, 10000))
        mariadb.add_user("John Doe", f"{user_name}", "john@nowhere.com", 123456789, "M", "test12345", "1,23,45,67,89,100", "2020-03-01")
        returned_value= mariadb.get_data(user_name, 'user_name', user_name)
        self.assertEqual(str(returned_value[0]), user_name)

if __name__ == "__main__":
    unittest.main()