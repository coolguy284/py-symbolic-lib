from src import *

def print_all_representations(symbolic_object):
  print(repr(symbolic_object))
  print(str(symbolic_object))
  print(symbolic_object.to_string_latex())
  print()

x = variables.x
y = variables.y
z = variables.z

print_all_representations(x)

print_all_representations(x + y + z)
print_all_representations(x * y + z)
print_all_representations(integer(-1))
print_all_representations(x * y - z)
print_all_representations(x**2 - 2*x - 4)
print_all_representations(2**x**2 - 2)
