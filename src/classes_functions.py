from .classes import *

def attempt_conversion_to_symbolic_type(value):
  if isinstance(value, int):
    return integer(value)
  
  return NotImplemented
