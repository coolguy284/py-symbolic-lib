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

def _operator_left_maker(operator_func):
  def operator_func_processed(object_two, object_one):
    object_one, object_two = _operator_conversion_to_symbolic_type(object_one, object_two)
    if object_one is NotImplemented or object_two is NotImplemented:
      return NotImplemented
    
    return operator_func(object_one, object_two)
  
  #operator_func_processed.__name__ = 'operator_left_' + '_'.join(operator_func.__name__.split('_')[1:])
  
  return operator_func_processed

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
  
  #cls.equal = operator_equal
  #cls.eq = operator_equal
  #cls.not_equal = operator_not_equal
  #cls.ne = operator_not_equal
  #cls.greater_than = operator_greater_than
  #cls.gt = operator_greater_than
  #cls.less_than = operator_less_than
  #cls.lt = operator_less_than
  #cls.greater_than_or_equal = operator_greater_than_or_equal
  #cls.ge = operator_greater_than_or_equal
  #cls.less_than_or_equal = operator_less_than_or_equal
  #cls.le = operator_less_than_or_equal
  
  cls.__pos__ = operator_identity
  cls.__neg__ = operator_unary_minus
  
  cls.__add__ = operator_add
  cls.__sub__ = operator_sub
  cls.__mul__ = operator_mul
  cls.__truediv__ = operator_div
  cls.__pow__ = operator_pow
  
  #cls.__eq__ = operator_equal
  #cls.__ne__ = operator_not_equal
  #cls.__gt__ = operator_greater_than
  #cls.__lt__ = operator_less_than
  #cls.__ge__ = operator_greater_than_or_equal
  #cls.__le__ = operator_less_than_or_equal
  
  cls.__radd__ = operator_left_add
  cls.__rsub__ = operator_left_sub
  cls.__rmul__ = operator_left_mul
  cls.__rtruediv__ = operator_left_div
  cls.__rpow__ = operator_left_pow
  
  #cls.__req__ = operator_left_equal
  #cls.__rne__ = operator_left_not_equal
  #cls.__rgt__ = operator_left_greater_than
  #cls.__rlt__ = operator_left_less_than
  #cls.__rge__ = operator_left_greater_than_or_equal
  #cls.__rle__ = operator_left_less_than_or_equal
  
  return cls
