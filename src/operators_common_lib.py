from . import basic

operator_valid_types = None

def _operator_get_valid_types():
  global operator_valid_types
  
  if operator_valid_types is None:
    operator_valid_types = basic.integer, basic.variable, basic.additive_group, basic.multiplicative_group, basic.fraction, basic.exponential
  
  return operator_valid_types

def _operator_conversion_to_symbolic_type(object_one, object_two):
  if not isinstance(object_one, _operator_get_valid_types()):
    object_one = basic.attempt_conversion_to_symbolic_type(object_one)
  
  if not isinstance(object_two, _operator_get_valid_types()):
    object_two = basic.attempt_conversion_to_symbolic_type(object_two)
  
  return object_one, object_two

def _operator_left_maker(operator_func):
  def operator_func_processed(object_two, object_one):
    object_one, object_two = _operator_conversion_to_symbolic_type(object_one, object_two)
    if object_one is NotImplemented or object_two is NotImplemented:
      return NotImplemented
    
    return operator_func(object_one, object_two)
  
  #operator_func_processed.__name__ = 'operator_left_' + '_'.join(operator_func.__name__.split('_')[1:])
  
  return operator_func_processed
