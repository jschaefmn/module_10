class Greeter:
  # def __init__(self, name):
    # self.name = name
  
  def __init__(self, input_name, puncuation):
    self.name = input_name
    self.punctuation = puncuation
    
  def morning_greeting(self):
    print(f'Good morning, {self.name}{self.punctuation}')
    
  def evening_greeting(self):
    print(f'Good morning, {self.name}{self.punctuation}')
    
example_greeter1 = Greeter('Erik', '.')
example_greeter2 = Greeter('Joey', '!')

example_greeter1.morning_greeting()
example_greeter2.morning_greeting()

# print(
#   example_greeter1.name
# )

