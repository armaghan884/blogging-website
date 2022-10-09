class Friends:
    def __init__(self, request_friend_id=0, requests=None):
        self.request_friend_id = request_friend_id
        self.requests = requests
    @property
    def request_friend_id(self):
        if self._request_friend_id == 0:
            return None
        return self._request_friend_id
    @request_friend_id.setter
    def request_friend_id(self, value):
        if not isinstance(value, int):
            raise TypeError("Request friend id must be an integer")
        elif not value:
            raise ValueError("Request friend id cannot be empty")
        self._request_friend_id = value


    @property
    def requests(self):
        return self._requests
    @requests.setter
    def requests(self, value):
        if not isinstance(value, list):
            raise TypeError("Requests must be a list")
        elif not all([isinstance(item, int) for item in value]):
            raise TypeError("Requests must be a list of integers")
        elif len(value) == 0:
            raise ValueError("Requests cannot be empty")
        self._requests = value



    
    
        
    