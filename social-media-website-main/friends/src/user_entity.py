from address_vo import Address
from friends_vo import Friends


class User:
    def __init__(self, id, name,
                 user_name, email, 
                 phone, gender, password, 
                 address, friend, warning,
                 is_active=True
                ):
        self.id = id
        self.name = name
        self.user_name = user_name
        self.email = email
        self.phone = phone
        self.gender = gender
        self.password = password
        self.address = address
        self.friend = friend
        self.warning = warning
        self.is_active = is_active
    
    def change_name(self, name):
        self.name = name
    
    def change_user_name(self, user_name):
        self.user_name = user_name
    
    def change_email(self, email):
        self.email = email
    
    def change_password(self, password):
        self.password = password

    def change_phone(self, phone):
        self.phone = phone
    
    def change_gender(self, gender):
        self.gender = gender

    def change_address(self, address):
        self.address = address
    
    def add_warning(self, warning):
        self.warning = warning
    
    def activate(self):
        self.is_active = True
    
    def deactivate(self):
        self.is_active = False

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("Id must be an integer")
        elif not value:
            raise ValueError("Id cannot be empty")
        self._id = value
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        elif not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        if not isinstance(value, str):
            raise TypeError("User name must be a string")
        elif not value:
            raise ValueError("User name cannot be empty")
        self._user_name = value
    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError("Email must be a string")
        elif not value:
            raise ValueError("Email cannot be empty")
        self._email = value
    
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if not isinstance(value, str):
            raise TypeError("Phone must be a string")
        elif not value:
            raise ValueError("Phone cannot be empty")
        self._phone = value
    
    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self, value):
        if not isinstance(value, str):
            raise TypeError("Gender must be a string")
        elif not value:
            raise ValueError("Gender cannot be empty")
        elif value not in ['M', 'F']:
            raise ValueError("Gender must be M or F")
        self._gender = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError("Password must be a string")
        elif not value:
            raise ValueError("Password cannot be empty")
        self._password = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if not isinstance(value, Address):
            raise TypeError("Address must be an Address object")
        elif not value:
            raise ValueError("Address cannot be empty")
        self._address = value

    @property
    def friend(self):
        return self._friend
    
    @friend.setter
    def friend(self, value):
        if not isinstance(value, Friends):
            raise TypeError("Friend must be from a Friends object")
        elif not value:
            raise ValueError("Friend cannot be empty")
        self._friend = value

    @property
    def warning(self):
        return self._warning

    @warning.setter
    def warning(self, value):
        if not isinstance(value, int):
            raise TypeError("Warning must be a int")
        elif not value:
            raise ValueError("Warning cannot be empty")
        self._warning = value
    
    @property
    def is_active(self):
        return self._is_active
    
    @is_active.setter
    def is_active(self, value):
        if not isinstance(value, bool):
            raise TypeError("Is active must be a boolean")
        self._is_active = value

