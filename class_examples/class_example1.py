class Car:
  def __init__(self,make, model, year):
    self.make = make
    self.model = model
    self.year = year
    
  def basic_info(self):
    print(f'The basic info of the car is a {self.make} {self.model} {self.year}')
    
example_car1 = Car('Ford', 'Focus', '2019')

example_car1.basic_info()