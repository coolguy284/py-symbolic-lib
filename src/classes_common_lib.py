from .operators import add_operators_to_class

def full_symbolic_class_decoration(cls):
  cls = add_operators_to_class(cls)
  
  if not hasattr(cls, 'to_string_repr'):
    raise Exception(f'to_string_repr not found on class {cls.__name__}')
  
  if not hasattr(cls, 'to_string_basic_textual'):
    raise Exception(f'to_string_basic_textual not found on class {cls.__name__}')
  
  if not hasattr(cls, 'to_string_latex'):
    raise Exception(f'to_string_latex not found on class {cls.__name__}')
    
  if not hasattr(cls, 'hash'):
    raise Exception(f'hash not found on class {cls.__name__}')
  
  cls.__repr__ = cls.to_string_repr
  cls.__str__ = cls.to_string_basic_textual
  cls.__hash__ = cls.hash
  
  return cls
