class Cat:
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
    print(f'The cat makes a {self._sound} sound.')
    
    
    
class Bird:
  def __init__(self, name, sound, wingspan):
    self._name = name
    self._sound = sound
    self._wingspan = wingspan
    
  def get_name(self):
    return self._name

  def set_name(self, new_name):
    if type(new_name) != str:
      print('Please type a new name')
    else:
      self._name = new_name
  
  def make_sound(self):
    print(f'The bird makes a {self._sound} sound.')
    
cat = Cat('Ronny', 'meow')
bird = Bird('Flyky', 'CA-CAW', 600)

cat.make_sound()
bird.make_sound()