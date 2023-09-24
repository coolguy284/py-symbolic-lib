from .classes_common_lib import full_symbolic_class_decoration
from .classes_abstract_base import symbolic_wrapper

@full_symbolic_class_decoration
class integer(symbolic_wrapper):
  '''
    py-symbolic-lib: integer class
    
    This class is a passthrough class for integers.
  '''
  
  __slots__ = 'value',
  
  @classmethod
  def from_integer(cls, value: int):
    integer_object = super(integer, cls).__new__(cls)
    
    integer_object.value = value
    
    return integer_object
  
  def to_string_repr(self):
    return f'integer({self.value})'
  
  def to_string_basic(self):
    return repr(self.value)
  
  def to_string_compact(self):
    return repr(self.value)
  
  def to_string_latex(self):
    return repr(self.value)
  
  def get_value(self):
    return self.value
  
  def get_hashable_form(self):
    return 'integer', self.value
  
  def __new__(cls, value: int):
    return cls.from_integer(value)
