import unittest
from user_entity import User
from address_vo import Address
from friends_vo import Friends
from post_entity import Post
class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.STREET_NAME = "Street name"
        self.STREET_NUMBER = 1
        self.CITY = "City"
        self.POST_CODE = "123456789"
        self.COUNTRY = "Country"
        self.ID = 1
        self.POST_ID = 1;
        self.NAME = "Name"
        self.USER_NAME = "User name"
        self.EMAIL = "Email"
        self.PHONE = "123456789"
        self.GENDER = "M"
        self.PASSWORD = "Password"
        self.FRIENDS_LIST = [1,2,3,4]
        self.REPORT_ID = 1;
        self.POST_IMAGE = "./user/hello.jpg"
        self.POST_TEXT = "Post"
        self.f = Friends(self.ID, self.FRIENDS_LIST)
        self.FRIENDS = self.f
        self.WARNING = 1
        self.a = Address(self.STREET_NAME, self.STREET_NUMBER, self.CITY, self.POST_CODE, self.COUNTRY)
        self.u = User(self.ID, self.NAME, self.USER_NAME, self.EMAIL, self.PHONE, self.GENDER, self.PASSWORD, self.a, self.FRIENDS, self.WARNING)
        self.p = Post(self.POST_ID, self.ID, self.REPORT_ID, self.POST_TEXT, self.POST_IMAGE)
    
    def test_Address_instantiation(self):
        self.assertEqual(self.a.street_name, self.STREET_NAME)
        self.assertEqual(self.a.street_number, self.STREET_NUMBER)
        self.assertEqual(self.a.city, self.CITY)
        self.assertEqual(self.a.post_code, self.POST_CODE)
        self.assertEqual(self.a.country, self.COUNTRY)

    def test_User_instantiation(self):
        self.assertEqual(self.u.id, self.ID)
        self.assertEqual(self.u.name, self.NAME)
        self.assertEqual(self.u.user_name, self.USER_NAME)
        self.assertEqual(self.u.email, self.EMAIL)
        self.assertEqual(self.u.phone, self.PHONE)
        self.assertEqual(self.u.gender, self.GENDER)
        self.assertEqual(self.u.password, self.PASSWORD)
        self.assertEqual(self.u.address.street_name, self.STREET_NAME)
        self.assertEqual(self.u.address.street_number, 1)
        self.assertEqual(self.u.address.city, self.CITY)
        self.assertEqual(self.u.address.post_code, self.POST_CODE)
        self.assertEqual(self.u.address.country, self.COUNTRY)
        self.assertEqual(self.u.friend.requests,self.FRIENDS_LIST)
        self.assertEqual(self.u.warning, self.WARNING)
        self.assertEqual(self.u.warning, True)

    def test_Friends_instantiation(self):
        self.assertEqual(self.f.request_friend_id, self.ID)
        self.assertEqual(self.f.requests, self.FRIENDS_LIST)

    def test_Post_instantiation(self):
        self.assertEqual(self.p.id, self.POST_ID)
        self.assertEqual(self.p.user_id, self.ID)
        self.assertEqual(self.p.report_id, self.REPORT_ID)
        self.assertEqual(self.p.text, self.POST_TEXT)
        self.assertEqual(self.p.image, self.POST_IMAGE)
        
    def test_Address_invalid(self):
        with self.assertRaises(TypeError):
            Address(1, self.STREET_NUMBER, self.CITY, self.POST_CODE, self.COUNTRY)
        with self.assertRaises(ValueError):
            Address(str(), self.STREET_NUMBER, self.CITY, self.POST_CODE, self.COUNTRY)
        with self.assertRaises(TypeError):
            Address(self.STREET_NAME, "1", self.CITY, self.POST_CODE, self.COUNTRY)
        with self.assertRaises(ValueError):
            Address(self.STREET_NAME, int(), self.CITY, self.POST_CODE, self.COUNTRY)
        with self.assertRaises(TypeError):
            Address(self.STREET_NAME, self.STREET_NUMBER, 1, self.POST_CODE, self.COUNTRY)
        with self.assertRaises(ValueError):
            Address(self.STREET_NAME, self.STREET_NUMBER, str(), self.POST_CODE, self.COUNTRY)
        with self.assertRaises(TypeError):
            Address(self.STREET_NAME, self.STREET_NUMBER, self.CITY, 1, self.COUNTRY)
        with self.assertRaises(ValueError):
            Address(self.STREET_NAME, self.STREET_NUMBER, self.CITY, str(), self.COUNTRY)
        with self.assertRaises(TypeError):
            Address(self.STREET_NAME, self.STREET_NUMBER, self.CITY, self.POST_CODE, 1)
        with self.assertRaises(ValueError):
            Address(self.STREET_NAME, self.STREET_NUMBER, self.CITY, self.POST_CODE, str())


    def test_User_invalid(self):
        with self.assertRaises(TypeError):
            User("", self.NAME, self.USER_NAME, self.EMAIL, self.PHONE, self.GENDER, self.PASSWORD, self.a, self.FRIENDS, self.WARNING)
        with self.assertRaises(ValueError):
            User(int(), self.NAME, self.USER_NAME, self.EMAIL, self.PHONE, self.GENDER, self.PASSWORD, self.a, self.FRIENDS, self.WARNING)
        with self.assertRaises(TypeError):
            User(self.ID, 1, self.USER_NAME, self.EMAIL, self.PHONE, self.GENDER, self.PASSWORD, self.a, self.FRIENDS, self.WARNING)
        with self.assertRaises(ValueError):
            User(self.ID, "", self.USER_NAME, self.EMAIL, self.PHONE, self.GENDER, self.PASSWORD, self.a, self.FRIENDS, self.WARNING)
        with self.assertRaises(TypeError):
            User(self.ID, self.NAME, 1, self.EMAIL, self.PHONE, self.GENDER, self.PASSWORD, self.a, self.FRIENDS, self.WARNING)
        with self.assertRaises(ValueError):
            User(self.ID, self.NAME, "", self.EMAIL, self.PHONE, self.GENDER, self.PASSWORD, self.a, self.FRIENDS, self.WARNING)
        with self.assertRaises(TypeError):
            User(self.ID, self.NAME, self.USER_NAME, self.EMAIL, 1, self.GENDER, self.PASSWORD, self.a, self.FRIENDS, self.WARNING)
        with self.assertRaises(ValueError):
            User(self.ID, self.NAME, self.USER_NAME, self.EMAIL, "", self.GENDER, self.PASSWORD, self.a, self.FRIENDS, self.WARNING)
        with self.assertRaises(TypeError):
            User(self.ID, self.NAME, 1, self.EMAIL, self.PHONE, 1, self.PASSWORD, self.a, self.FRIENDS, self.WARNING)
        with self.assertRaises(ValueError):
            User(self.ID, self.NAME, "", self.EMAIL, self.PHONE, "", self.PASSWORD, self.a, self.FRIENDS, self.WARNING)
        with self.assertRaises(ValueError):
            User(self.ID, self.NAME, "", self.EMAIL, self.PHONE, "A", self.PASSWORD, self.a, self.FRIENDS, self.WARNING)
        with self.assertRaises(TypeError):
            User(self.ID, self.NAME, 1, self.EMAIL, self.PHONE, self.GENDER, 1, self.a, self.FRIENDS, self.WARNING)
        with self.assertRaises(ValueError):
            User(self.ID, self.NAME, "", self.EMAIL, self.PHONE, self.GENDER, "", self.a, self.FRIENDS, self.WARNING)
        with self.assertRaises(TypeError):
            User(self.ID, self.NAME, 1, self.EMAIL, self.PHONE, self.GENDER, 1, self.a, 1, self.WARNING)
        with self.assertRaises(ValueError):
            User(self.ID, self.NAME, "", self.EMAIL, self.PHONE, self.GENDER, self.PASSWORD, self.a, "", self.WARNING)
        with self.assertRaises(TypeError):
            User(self.ID, self.NAME, 1, self.EMAIL, self.PHONE, self.GENDER, 1, self.a, self.FRIENDS, "a")
        with self.assertRaises(ValueError):
            User(self.ID, self.NAME, "", self.EMAIL, self.PHONE, self.GENDER, self.PASSWORD, self.a, self.FRIENDS, int())
        with self.assertRaises(TypeError):
            User(self.ID, self.NAME, 1, self.EMAIL, self.PHONE, self.GENDER, 1, self.a, self.FRIENDS, self.WARNING, "True")
        with self.assertRaises(ValueError):
            User(self.ID, self.NAME, "", self.EMAIL, self.PHONE, self.GENDER, self.PASSWORD, self.a, self.FRIENDS, self.WARNING,bool())
    
    def test_Friends_invalid(self):
        with self.assertRaises(TypeError):
            Friends("1", self.FRIENDS_LIST)
        with self.assertRaises(ValueError):
            Friends(int(), self.FRIENDS_LIST)
        with self.assertRaises(TypeError):
            Friends(self.ID, 1)
        with self.assertRaises(TypeError):            
            Friends(self.ID, ["1"])
        with self.assertRaises(ValueError):
            Friends(self.ID, list())
    
    def test_User_change(self):
        self.u.id = 2
        self.u.name = "New name"
        self.u.user_name = "New user name"
        self.u.email = "New email"
        self.u.phone = "New phone"
        self.u.gender = "F"
        self.u.password = "New password"
        self.u.address.street_name = "New street name"
        self.u.address.street_number = 2
        self.u.address.city = "New city"
        self.u.address.post_code = "New post code"
        self.u.address.country = "New country"
        self.u.friend = self.f = Friends(2, self.FRIENDS_LIST)
        self.u.warning = 2
        self.u.deactivate()

        self.assertEqual(self.u.name, "New name")
        self.assertEqual(self.u.user_name, "New user name")
        self.assertEqual(self.u.email, "New email")
        self.assertEqual(self.u.phone, "New phone")
        self.assertEqual(self.u.gender, "F")
        self.assertEqual(self.u.password, "New password")
        self.assertEqual(self.u.address.street_name, "New street name")
        self.assertEqual(self.u.address.street_number, 2)
        self.assertEqual(self.u.address.city, "New city")
        self.assertEqual(self.u.address.post_code, "New post code")
        self.assertEqual(self.u.address.country, "New country")
        self.assertEqual(self.u.friend.requests,[1,2,3,4])
        self.assertEqual(self.u.warning, 2)
        self.assertEqual(self.u.is_active, False)

    def test_Friends_change(self):
        self.f.request_friend_id = 2
        self.f.requests = [5, 6, 7, 8]
        self.assertEqual(self.f.request_friend_id, 2)
        self.assertEqual(self.f.requests, [5, 6, 7, 8])

   

if __name__ == "__main__":
    unittest.main()
