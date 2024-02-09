class Pet: # Super/Parent class
  def __init__(self, name, sound):
    self._name = name
    self._sound = sound
    
  def get_name(self):
    return self._name

  def set_name(self, new_name):
    if type(new_name) != str:
      print('Please type a new name')
    else:
      self._name = new_name
      
  def make_sound(self):
    print(f'{self._sound}')
    
class Cat(Pet): # Sub/Child class
  pass

class Bird(Pet): # Sub/child class
  def __init__(self, name, sound, wingspan):
    super().__init__(name,sound)
    self._wingspan = wingspan
    
class Turtle(Pet):
  def run(self):
    print('The turtle does what? RUN ')
    
  def make_sound(self):
    print('Turtles do not make sound')

cat = Cat('Ronny', 'meow')
bird = Bird('Flyky', 'CA-CAW', 600)
turtle = Turtle('Speedy', 'turtle noises')

cat.make_sound()
bird.make_sound()
turtle.run()
turtle.make_sound()