# Python Packages

# The Python Package Index (PyPI) is a repository of software for the Python programming language. - https://pypi.org/

# Packages that are not come with Python by default, need to be installed by pip/pip3 package manager.

# Syntax: pip3 install <PackageName> - Mac or Linux
#         pip install <PackageName> - Windows

# For Example Package: pip3 install prettytable
# As I'm using linux

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)

# Output:

# +--------------+----------+
# | Pokemon Name |   Type   |
# +--------------+----------+
# |   Pikachu    | Electric |
# |   Squirtle   |  Water   |
# |  Charmander  |   Fire   |
# +--------------+----------+

table.align = "l" # Left Align

print(table)

# Output:
# +--------------+----------+
# | Pokemon Name | Type     |
# +--------------+----------+
# | Pikachu      | Electric |
# | Squirtle     | Water    |
# | Charmander   | Fire     |
# +--------------+----------+