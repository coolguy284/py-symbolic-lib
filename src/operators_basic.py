from . import classes

from .operators_common_lib import _operator_conversion_to_symbolic_type_single, _operator_conversion_to_symbolic_type_multiple, _operator_left_maker

def operator_add(object_one, object_two):
  object_one, object_two = _operator_conversion_to_symbolic_type_multiple(object_one, object_two)
  if object_one is NotImplemented or object_two is NotImplemented:
    return NotImplemented
  
  if isinstance(object_one, classes.additive_group):
    if isinstance(object_two, classes.additive_group):
      return classes.additive_group(*object_one.get_elements(), *object_two.get_elements())
    else:
      return classes.additive_group(*object_one.get_elements(), object_two)
  else:
    if isinstance(object_two, classes.additive_group):
      return classes.additive_group(object_one, *object_two.get_elements())
    else:
      return classes.additive_group(object_one, object_two)

def operator_sub(object_one, object_two):
  return object_one + -object_two

def operator_mul(object_one, object_two):
  object_one, object_two = _operator_conversion_to_symbolic_type_multiple(object_one, object_two)
  if object_one is NotImplemented or object_two is NotImplemented:
    return NotImplemented
  
  if isinstance(object_one, classes.multiplicative_group):
    if isinstance(object_two, classes.multiplicative_group):
      return classes.multiplicative_group(*object_one.get_elements(), *object_two.get_elements())
    else:
      return classes.multiplicative_group(*object_one.get_elements(), object_two)
  else:
    if isinstance(object_two, classes.multiplicative_group):
      return classes.multiplicative_group(object_one, *object_two.get_elements())
    else:
      return classes.multiplicative_group(object_one, object_two)

def operator_div(object_one, object_two):
  object_one, object_two = _operator_conversion_to_symbolic_type_multiple(object_one, object_two)
  if object_one is NotImplemented or object_two is NotImplemented:
    return NotImplemented
  
  return classes.fraction(object_one, object_two)

def operator_pow(object_one, object_two):
  object_one, object_two = _operator_conversion_to_symbolic_type_multiple(object_one, object_two)
  if object_one is NotImplemented or object_two is NotImplemented:
    return NotImplemented
  
  return classes.exponential(object_one, object_two)

def operator_identity(object_one):
  return object_one

def operator_unary_minus(object_one):
  object_one = _operator_conversion_to_symbolic_type_single(object_one)
  if object_one is NotImplemented:
    return NotImplemented
  
  return classes.unary_minus(object_one)

#def operator_equal(object_one, object_two):
#  object_one, object_two = _operator_conversion_to_symbolic_type_multiple(object_one, object_two)
#  if object_one is NotImplemented or object_two is NotImplemented:
#    return NotImplemented
#  
#  return classes.equal(object_one, object_two)
#
#def operator_not_equal(object_one, object_two):
#  object_one, object_two = _operator_conversion_to_symbolic_type_multiple(object_one, object_two)
#  if object_one is NotImplemented or object_two is NotImplemented:
#    return NotImplemented
#  
#  return classes.not_equal(object_one, object_two)
#
#def operator_greater_than(object_one, object_two):
#  object_one, object_two = _operator_conversion_to_symbolic_type_multiple(object_one, object_two)
#  if object_one is NotImplemented or object_two is NotImplemented:
#    return NotImplemented
#  
#  return classes.greater_than(object_one, object_two)
#
#def operator_less_than(object_one, object_two):
#  object_one, object_two = _operator_conversion_to_symbolic_type_multiple(object_one, object_two)
#  if object_one is NotImplemented or object_two is NotImplemented:
#    return NotImplemented
#  
#  return classes.less_than(object_one, object_two)
#
#def operator_greater_than_or_equal(object_one, object_two):
#  object_one, object_two = _operator_conversion_to_symbolic_type_multiple(object_one, object_two)
#  if object_one is NotImplemented or object_two is NotImplemented:
#    return NotImplemented
#  
#  return classes.greater_than_or_equal(object_one, object_two)
#
#def operator_less_than_or_equal(object_one, object_two):
#  object_one, object_two = _operator_conversion_to_symbolic_type_multiple(object_one, object_two)
#  if object_one is NotImplemented or object_two is NotImplemented:
#    return NotImplemented
#  
#  return classes.less_than_or_equal(object_one, object_two)

operator_left_add = _operator_left_maker(operator_add)
operator_left_sub = _operator_left_maker(operator_sub)
operator_left_mul = _operator_left_maker(operator_mul)
operator_left_div = _operator_left_maker(operator_div)
operator_left_pow = _operator_left_maker(operator_pow)
#operator_left_equal = _operator_left_maker(operator_equal)
#operator_left_not_equal = _operator_left_maker(operator_not_equal)
#operator_left_greater_than = _operator_left_maker(operator_greater_than)
#operator_left_less_than = _operator_left_maker(operator_less_than)
#operator_left_greater_than_or_equal = _operator_left_maker(operator_greater_than_or_equal)
#operator_left_less_than_or_equal = _operator_left_maker(operator_less_than_or_equal)
