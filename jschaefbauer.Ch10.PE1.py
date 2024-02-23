class Pet:
  # Data attributes
  #__name
  #__animalType
  #age
  
  # Pet definition
  def __init__(self, name, type, age):
    self._name = name
    self._animal_type = type
    self._age = age
    
  # Getters
  def get_name(self):
    return self._name
  
  def get_animal_type(self):
    return self._animal_type
  
  def get_age(self):
    return self._age
  
  # Setters
  def set_name(self, name):
    self._name = name
  
  def set_animal_type(self, type):
    self._animal_type = type
  
  def set_age(self, age):
    self._age = age
    
# Program logic
def main():
  # Testing getters
  name = input("Enter your pet's name: ")
  type = input("Enter your pet's animal type: ")
  age = int(input("Enter your pet's age: "))
  pet = Pet(name, type, age)
  
  # print(pet.get_name(), pet.get_animal_type(), pet.get_age())
  
  # Testing setters
  pet.set_name('Otis')
  pet.set_animal_type('pug')
  pet.set_age('4')
  print(pet.get_name(), pet.get_animal_type(), pet.get_age())
  
if __name__ == '__main__':
  main()