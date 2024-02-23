class Person:
  def __init__(self, input_name, input_age):
    # self.name = input_name
    self._name = input_name # privage attribute
    # self.age = input_age
    self._age = input_age # Private attribute
    
  # Name getter
  def get_name(self):
    return self._name
  
  # Age getter
  def get_age(self):
    return int(self._age)
  
  # Age setter
  def set_age(self, new_age):
    if type(new_age) != int or new_age < 0:
      print('Must be positive integer')
    else:
      self._age = new_age 
      
    
me = Person('Jake', 24)

print(f'{me._name} is {me._age} years old')
me.set_age(-25)
print(f'{me._name} is {me._age} years old')

