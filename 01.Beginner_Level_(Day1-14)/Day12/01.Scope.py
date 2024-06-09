# Scope

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope

def drink_potion():
  potion_strength = 2 # Local var
  print(potion_strength)

drink_potion()
# print(potion_strength) # Error

# Global Scope
player_health = 10 # Global var

def drink_potion():
  potion_strength = 2 # Local var
  print(player_health)

drink_potion()

# Modify a Global Variable

enemies = 1

def increase_enemies():
  global enemies
  enemies += 1
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Global Constants

# Naming Constants uppercase helps in better understanding.
PI = 3.141
