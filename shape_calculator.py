class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def set_width(self, value):
    self.width = value

  def set_height(self, value):
    self.height = value
  
  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (self.width*2 + self.height*2)

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):

    if self.width > 50:
      return "Too big for picture."
    elif self.height > 50:
      return "Too big for picture."

    picture_string = ""
    i = 0
    height = self.height
    width = self.width

    while i < height:
      picture_string += "*" * width + "\n"
      i += 1
    return picture_string

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"


  def get_amount_inside(self, shape2):
    q_width = (self.width - (self.width % shape2.width ) ) / shape2.width
    q_heigth = (self.height - (self.height % shape2.height) ) / shape2.height
    return q_width * q_heigth



class Square(Rectangle):
  def __init__(self, value):
    self.width = value
    self.height = value

  def set_side(self, value):
    self.width = value
    self.height = value

  def set_width(self, value):
    self.width = value
    self.height = value

  def set_height(self, value):
    self.width = value
    self.height = value
  
  def __str__(self):
    return f"Square(side={self.width})"
