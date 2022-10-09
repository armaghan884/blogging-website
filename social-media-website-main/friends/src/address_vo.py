class Address:
    def __init__(self, street_name, street_number, city, post_code, country):
        self.street_name = self._validate_street_name(street_name)
        self.street_number = self._validate_street_number(street_number)
        self.city = self._validate_city(city)
        self.post_code = self._validate_post_code(post_code)
        self.country = self._validate_country(country)


    def _validate_street_name(self, street_name):
        if not isinstance(street_name, str):
            raise TypeError("Street name must be a string")
        elif not street_name:
            raise ValueError("Street name cannot be empty")
        return street_name
    
    def _validate_street_number(self, street_number):
        if not isinstance(street_number, int):
            raise TypeError("Street number must be an integer")
        elif not street_number:
            raise ValueError("Street number cannot be empty")
        return street_number
    
    def _validate_city(self, city):
        if not isinstance(city, str):
            raise TypeError("City must be a string")
        elif not city:
            raise ValueError("City cannot be empty")
        return city
    
    def _validate_post_code(self, post_code):
        if not isinstance(post_code, str):
            raise TypeError("Post code must be a string")
        elif not post_code:
            raise ValueError("Post code cannot be empty")
        return post_code
    
    def _validate_country(self, country):
        if not isinstance(country, str):
            raise TypeError("Country must be a string")
        elif not country:
            raise ValueError("Country cannot be empty")
        return country
            