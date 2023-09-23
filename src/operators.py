from . import basic

operator_valid_types = None

def operator_get_valid_types():
  global operator_valid_types
  
  if operator_valid_types is None:
    operator_valid_types = basic.integer, basic.variable, basic.additive_group, basic.multiplicative_group, basic.fraction, basic.exponential
  
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

def _operator_left_maker(operator_func):
  def operator_func_processed(object_two, object_one):
    object_one, object_two = _operator_conversion_to_symbolic_type(object_one, object_two)
    if object_one is NotImplemented or object_two is NotImplemented:
      return NotImplemented
    
    return operator_func(object_one, object_two)
  
  return operator_func_processed

operator_left_add = _operator_left_maker(operator_add)
operator_left_sub = _operator_left_maker(operator_sub)
operator_left_mul = _operator_left_maker(operator_mul)
operator_left_div = _operator_left_maker(operator_div)
operator_left_pow = _operator_left_maker(operator_pow)

def add_operators_to_class(cls):
  cls.identity = operator_identity
  cls.unary_plus = operator_identity
  cls.pos = operator_identity
  cls.unary_minus = operator_unary_minus
  cls.neg = operator_unary_minus
  
  cls.add = operator_add
  cls.sub = operator_sub
  cls.mul = operator_mul
  cls.div = operator_div
  cls.truediv = operator_div
  cls.pow = operator_pow
  
  cls.__pos__ = operator_identity
  cls.__neg__ = operator_unary_minus
  
  cls.__add__ = operator_add
  cls.__sub__ = operator_sub
  cls.__mul__ = operator_mul
  cls.__truediv__ = operator_div
  cls.__pow__ = operator_pow
  
  cls.__radd__ = operator_left_add
  cls.__rsub__ = operator_left_sub
  cls.__rmul__ = operator_left_mul
  cls.__rtruediv__ = operator_left_div
  cls.__rpow__ = operator_left_pow
  
  return cls
