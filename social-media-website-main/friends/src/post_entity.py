class Post:
    def __init__(self, id, user_id,
                report_id, text,
                image):

        self.id = id
        self.user_id = user_id
        self.report_id = report_id
        self.text = text
        self.image = image

def change_text(self, str):
    self.change_text = change_text

def change_image(self, int):
    self.change_image = change_image

def active(self):
    self.is_active = True

def deactivate(self):
    self.deactivate  = False

def is_active(self):
    self.is_active = True


@property
def id(self):
    return self.id

@id.setter
def id(self, id):
    if not isinstance(id,int):
        raise TypeError("id need to be an integer")
    elif not id:
        raise ValueError("id cannot be empty")
    self.id = id

@property
def user_id(self):
    return self.user_id

@user_id.setter
def user_id(self, user_id):
    if not isinstance(user_id,int):
        raise TypeError("user_id need to be a integer")
    elif not user_id:
        raise ValueError("user_id cannot be empty")
    self.user_id = user_id

@property
def report_id(self):
    return self.report_id

@report_id.setter
def report_id(self, report_id):
    if not isinstance(report_id,int):
        raise TypeError("report_id needs to be an integer")
    elif not report_id:
        raise ValueError("report_id cannot be empty")
    self.report_id = report_id

@property
def text(self):
    return self.text

@text.setter
def text(self, text):
    if not isinstance(text,str):
        raise TypeError("text needs to be a text field")
    elif not text:
        raise ValueError("text cannot be empty")
    self.text = text

@property
def image(self):
    return self.image

@image.setter 
def image(self, image):
    if not isinstance(image,str):
        raise TypeError("image needs to be a valid image type (.jpeg .bmp .tiff .raw .png or .gif) ")
    elif not image:
        raise ValueError("image cannot be empty")
    self.image = image
