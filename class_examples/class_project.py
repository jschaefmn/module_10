class Character:
  def __init__(self, name, armor, weapon, health):
    self._armor = armor
    self._weapon = weapon
    self._name = name
    self._health = health
    
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
    
  
class Armor:
  def __init__(self, name, defense):
    self._name = name
    self._defense = defense