from .operators import *

def full_symbolic_class_decoration(cls):
  cls = add_operators_to_class(cls)
  
  if not hasattr(cls, 'to_string_repr'):
    raise Exception(f'to_string_repr not found on class {cls.__name__}')
  
  if not hasattr(cls, 'to_string_basic_textual'):
    raise Exception(f'to_string_basic_textual not found on class {cls.__name__}')
  
  cls.__repr__ = cls.to_string_repr
  cls.__str__ = cls.to_string_basic_textual
  
  return cls

# creating an empty variable so the type annotation is happier, this is done for all the classes that need it
variable = None

@full_symbolic_class_decoration
class variable:
  '''
    py-symbolic-lib: variable class
    
    This class is for algebraic variables.
  '''
  
  __slots__ = 'variable_name',
  
  @classmethod
  def from_string(cls, variable_name: str) -> variable:
    variable_object = super(variable, cls).__new__(cls)
    
    variable_object.variable_name = variable_name
    
    return variable_object
  
  def to_string_repr(self):
    return f'variable(\'{self.variable_name}\')'
  
  def to_string_basic_textual(self):
    return self.variable_name
  
  def get_item(self):
    return self.variable_name
  
  def __new__(cls, variable_name: str) -> variable:
    return cls.from_string(variable_name)

class variables_factory:
  '''
    py-symbolic-lib: variable_factory class
    
    This class is for conveniently creating algebraic variables using dot or bracket notation, like so:
    
    >>> variables.x
    variable('x')
  '''
  
  __slots__ = ()
  
  def __getattr__(self, attribute_name: str) -> variable:
    return variable(attribute_name)
  
  def __setattr__(self, attribute_name: str):
    pass
  
  __delattr__ = __setattr__
  __getitem__ = __getattr__
  __setitem__ = __setattr__
  __delitem__ = __delattr__

variables = variables_factory()

additive_group = None

@full_symbolic_class_decoration
class additive_group:
  '''
    py-symbolic-lib: additive_group
    
    This class is to handle many symbols / expressions added together, like so:
    
    >>> variables.x + variables.y
    additive_group(variable('x'), variable('y'))
  '''
  
  __slots__ = 'elements',
  
  @classmethod
  def from_iterable(cls, iterable) -> additive_group:
    additive_group_object = super(additive_group, cls).__new__(cls)
    
    additive_group_object.elements = tuple(iterable)
    
    return additive_group_object
  
  def to_string_repr(self):
    return 'additive_group(' + ', '.join(map(lambda x: x.to_string_repr(), self.get_items())) + ')'
  
  def to_string_basic_textual(self):
    return ' + '.join(map(lambda x: x.to_string_basic_textual(), self.get_items()))
  
  def get_items(self):
    return self.elements
  
  def __new__(cls, *iterable) -> additive_group:
    return cls.from_iterable(iterable)
