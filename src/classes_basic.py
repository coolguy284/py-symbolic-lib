from .classes_common_lib import full_symbolic_class_decoration
from .classes_base import symbolic_basic

@full_symbolic_class_decoration
class variable(symbolic_basic):
  '''
    py-symbolic-lib: variable class
    
    This class is for algebraic variables.
  '''
  
  __slots__ = 'variable_name',
  
  @classmethod
  def from_string(cls, variable_name: str):
    variable_object = super(variable, cls).__new__(cls)
    
    variable_object.variable_name = variable_name
    
    return variable_object
  
  def to_string_repr(self):
    return f'variable(\'{self.variable_name}\')'
  
  def to_string_basic_textual(self):
    return self.variable_name
  
  def to_string_latex(self):
    return self.variable_name
  
  def get_item(self):
    return self.variable_name
  
  def get_hashable_form(self):
    return 'variable', self.variable_name
  
  def __new__(cls, variable_name: str):
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
