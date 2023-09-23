from . import basic

operator_valid_types = None

def operator_get_valid_types():
  global operator_valid_types
  
  if operator_valid_types is None:
    operator_valid_types = basic.integer, basic.variable, basic.additive_group, basic.multiplicative_group
  
  return operator_valid_types

def _operator_conversion_to_symbolic_type(object_one, object_two):
  if not isinstance(object_one, operator_get_valid_types()):
    object_one = basic.attempt_conversion_to_symbolic_type(object_one)
  
  if not isinstance(object_two, operator_get_valid_types()):
    object_two = basic.attempt_conversion_to_symbolic_type(object_two)
  
  return object_one, object_two

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

def operator_unary_minus(object_one):
  return -1 * object_one

def operator_left_add(object_two, object_one):
  object_one, object_two = _operator_conversion_to_symbolic_type(object_one, object_two)
  if object_one is NotImplemented or object_two is NotImplemented:
    return NotImplemented
  
  return object_one + object_two

def operator_left_sub(object_two, object_one):
  object_one, object_two = _operator_conversion_to_symbolic_type(object_one, object_two)
  if object_one is NotImplemented or object_two is NotImplemented:
    return NotImplemented
  
  return object_one - object_two

def operator_left_mul(object_two, object_one):
  object_one, object_two = _operator_conversion_to_symbolic_type(object_one, object_two)
  if object_one is NotImplemented or object_two is NotImplemented:
    return NotImplemented
  
  return object_one * object_two

def add_operators_to_class(cls):
  cls.__add__ = operator_add
  cls.__sub__ = operator_sub
  cls.__mul__ = operator_mul
  cls.__neg__ = operator_unary_minus
  
  cls.__radd__ = operator_left_add
  cls.__rsub__ = operator_left_sub
  cls.__rmul__ = operator_left_mul
  
  return cls
