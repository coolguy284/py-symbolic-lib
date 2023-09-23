from . import basic

def operator_add(object_one, object_two):
  valid_types = basic.variable, basic.additive_group
  
  if not isinstance(object_one, valid_types):
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

def add_operators_to_class(cls):
  cls.__add__ = operator_add
  return cls
