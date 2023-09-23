from . import basic

from .operators_common_lib import _operator_conversion_to_symbolic_type, _operator_left_maker

def operator_add(object_one, object_two):
  object_one, object_two = _operator_conversion_to_symbolic_type(object_one, object_two)
  if object_one is NotImplemented or object_two is NotImplemented:
    return NotImplemented
  
  if isinstance(object_one, basic.additive_group):
    if isinstance(object_two, basic.additive_group):
      return basic.additive_group(*object_one.get_items(), *object_two.get_items())
    else:
      return basic.additive_group(*object_one.get_items(), object_two)
  else:
    if isinstance(object_two, basic.additive_group):
      return basic.additive_group(object_one, *object_two.get_items())
    else:
      return basic.additive_group(object_one, object_two)

def operator_sub(object_one, object_two):
  return object_one + -object_two

def operator_mul(object_one, object_two):
  object_one, object_two = _operator_conversion_to_symbolic_type(object_one, object_two)
  if object_one is NotImplemented or object_two is NotImplemented:
    return NotImplemented
  
  if isinstance(object_one, basic.multiplicative_group):
    if isinstance(object_two, basic.multiplicative_group):
      return basic.multiplicative_group(*object_one.get_items(), *object_two.get_items())
    else:
      return basic.multiplicative_group(*object_one.get_items(), object_two)
  else:
    if isinstance(object_two, basic.multiplicative_group):
      return basic.multiplicative_group(object_one, *object_two.get_items())
    else:
      return basic.multiplicative_group(object_one, object_two)

def operator_div(object_one, object_two):
  object_one, object_two = _operator_conversion_to_symbolic_type(object_one, object_two)
  if object_one is NotImplemented or object_two is NotImplemented:
    return NotImplemented
  
  return basic.fraction(object_one, object_two)

def operator_pow(object_one, object_two):
  object_one, object_two = _operator_conversion_to_symbolic_type(object_one, object_two)
  if object_one is NotImplemented or object_two is NotImplemented:
    return NotImplemented
  
  return basic.exponential(object_one, object_two)

def operator_identity(object_one):
  return object_one

def operator_unary_minus(object_one):
  return -1 * object_one

#def operator_equal(object_one, object_two):
#  object_one, object_two = _operator_conversion_to_symbolic_type(object_one, object_two)
#  if object_one is NotImplemented or object_two is NotImplemented:
#    return NotImplemented
#  
#  return basic.equal(object_one, object_two)
#
#def operator_not_equal(object_one, object_two):
#  object_one, object_two = _operator_conversion_to_symbolic_type(object_one, object_two)
#  if object_one is NotImplemented or object_two is NotImplemented:
#    return NotImplemented
#  
#  return basic.not_equal(object_one, object_two)
#
#def operator_greater_than(object_one, object_two):
#  object_one, object_two = _operator_conversion_to_symbolic_type(object_one, object_two)
#  if object_one is NotImplemented or object_two is NotImplemented:
#    return NotImplemented
#  
#  return basic.greater_than(object_one, object_two)
#
#def operator_less_than(object_one, object_two):
#  object_one, object_two = _operator_conversion_to_symbolic_type(object_one, object_two)
#  if object_one is NotImplemented or object_two is NotImplemented:
#    return NotImplemented
#  
#  return basic.less_than(object_one, object_two)
#
#def operator_greater_than_or_equal(object_one, object_two):
#  object_one, object_two = _operator_conversion_to_symbolic_type(object_one, object_two)
#  if object_one is NotImplemented or object_two is NotImplemented:
#    return NotImplemented
#  
#  return basic.greater_than_or_equal(object_one, object_two)
#
#def operator_less_than_or_equal(object_one, object_two):
#  object_one, object_two = _operator_conversion_to_symbolic_type(object_one, object_two)
#  if object_one is NotImplemented or object_two is NotImplemented:
#    return NotImplemented
#  
#  return basic.less_than_or_equal(object_one, object_two)

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
