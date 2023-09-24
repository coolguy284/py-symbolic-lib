from src import *

def print_all_representations(symbolic_object):
  print(repr(symbolic_object))
  print(str(symbolic_object))
  print(symbolic_object.to_string_compact())
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
print_all_representations(x**2 - 2 * x - 4)
print_all_representations(2**x**2 - 2)
print_all_representations((2**x)**2 - 2)
expr = (2 * x + 1) / (y - 4)
print_all_representations(expr)

print(expr.get_hashable_form())
print()

print(x is x)
print(variables.x is variables.x)
print()

from src.operators_common_lib import operator_valid_types

for i in operator_valid_types:
  print(i.__name__, dict(i._instance_dict), sep = ': ')
