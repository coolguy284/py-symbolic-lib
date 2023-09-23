from .classes_common_lib import full_symbolic_class_decoration

@full_symbolic_class_decoration
class integer:
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
  
  def to_string_basic_textual(self):
    return repr(self.value)
  
  def to_string_latex(self):
    return repr(self.value)
  
  def get_value(self):
    return self.value
  
  def hash(self):
    return hash(('integer', self.value))
  
  def __new__(cls, value: int):
    return cls.from_integer(value)
