class Greeter:
  # def __init__(self, name):
    # self.name = name
  
  def __init__(self, input_name, puncuation): # Constructor
    self.name = input_name # Attribute
    self.punctuation = puncuation # Attribute
    
  def morning_greeting(self): # Instance Method
    print(f'Good morning, {self.name}{self.punctuation}')
    
  def evening_greeting(self): # Instance Method
    print(f'Good morning, {self.name}{self.punctuation}')
    
  def general_greeting(): # Static Method
    print("Hello, there")
    
example_greeter1 = Greeter('Erik', '.') #instance of greeter | greeter object
example_greeter2 = Greeter('Joey', '!') #instance of greeter | greeter object

example_greeter1.morning_greeting()
example_greeter2.morning_greeting()

Greeter.general_greeting()

# print(
#   example_greeter1.name
# )

