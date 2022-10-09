from user_entity import User
from address_vo import Address
from friends_vo import Friends
from mariadb_adapter import add_user, get_user

class User_repository:

    def __init__(self, user):
        self.user = user

    @classmethod
    def store_user(cls, user):
        cls.user = user
        response = cls.read_user("user_name")
        if not response:
            add_user(user.name, user.user_name, user.email, user.phone, user.gender, user.password, str(user.friend.requests), "2020-03-01")
            print('User added')
        return 'User added'

    @classmethod
    def read_user(cls, field, user = None, select = None):
        if user:
            cls.user = user
        response = get_user(cls.user.user_name, "user_name", "user_name")
        return response
        
        
            


    def remove_user():
        pass

    def find_user():
        pass

    def change_user():
        pass

    