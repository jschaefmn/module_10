class Person:
  def __init__(self, input_name, input_age):
    self.name = input_name
    self.age = input_age
    
  def get_name(self):
    return self.name
  
  def get_age(self):
    return int(self.age)
  
  def set_age(self, new_age):
    self.age = new_age 
    
me = Person('Jake', 24)

print(f'{me.name} is {me.age} years old')
me.set_age(25)
print(f'{me.name} is {me.age} years old')

