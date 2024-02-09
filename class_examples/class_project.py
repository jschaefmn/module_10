import random

class Character:
  def __init__(self, name, armor, weapon, health):
    self._armor = armor
    self._weapon = weapon
    self._name = name
    self._health = health
    
  def make_attack(self, other_character):
    damage = self._weapon.calculate_damage()
    print(f'{self.name} attacks with {self.weapon.name}')
    print(f'It does {damage} points of damage')    
    other_character.receive_attack(damage)
    
  def receive_attack(self, damage):
    block = self._armor.calculate_defense()
    damage -= block
    self._health -= damage
    if self._health <= 0:
      print(f'{self._name} has lost')
    
    
class Hero(Character):
  def __init__(self, name, armor, weapon, health, item):
    super().__init__(name, armor, weapon, health)
    self._item = item
  pass

class Enemy(Character):
  pass

class Weapon:
  def __init__(self, name, attack):
    self._name = name
    self._attack = attack
    
  def calculate_damage(self):
    lower_end = self.attack - 20
    higher_end = self.attack + 20
    return random.randrange(lower_end, higher_end)
    
  
class Armor:
  def __init__(self, name, defense):
    self._name = name
    self._defense = defense
    
  def calculate_armor(self):
    lower_end = self._defense - 5
    higher_end = self._defense + 5
    return random.randrange(lower_end, higher_end)