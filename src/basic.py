from .operators import *

def full_symbolic_class_decoration(cls):
  cls = add_operators_to_class(cls)
  
  if not hasattr(cls, 'to_string_repr'):
    raise Exception(f'to_string_repr not found on class {cls.__name__}')
  
  if not hasattr(cls, 'to_string_basic_textual'):
    raise Exception(f'to_string_basic_textual not found on class {cls.__name__}')
  
  if not hasattr(cls, 'to_string_latex'):
    raise Exception(f'to_string_latex not found on class {cls.__name__}')
  
  cls.__repr__ = cls.to_string_repr
  cls.__str__ = cls.to_string_basic_textual
  
  return cls

# class names are initially empty variable so the type annotation is happier, this is done for all the classes that need it

integer = None

@full_symbolic_class_decoration
class integer:
  '''
    py-symbolic-lib: integer class
    
    This class is a passthrough class for integers.
  '''
  
  __slots__ = 'value',
  
  @classmethod
  def from_integer(cls, value: int) -> integer:
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
  
  def __new__(cls, value: int) -> integer:
    return cls.from_integer(value)

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
  
  def to_string_latex(self):
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
  
  def to_string_latex(self):
    return '+'.join(map(lambda x: x.to_string_latex(), self.get_items()))
  
  def get_items(self):
    return self.elements
  
  def __new__(cls, *iterable) -> additive_group:
    return cls.from_iterable(iterable)

multiplicative_group = None

@full_symbolic_class_decoration
class multiplicative_group:
  '''
    py-symbolic-lib: multiplicative_group
    
    This class is to handle many symbols / expressions multiplied together, like so:
    
    >>> variables.x * variables.y
    multiplicative_group(variable('x'), variable('y'))
  '''
  
  __slots__ = 'elements',
  
  @classmethod
  def from_iterable(cls, iterable) -> multiplicative_group:
    multiplicative_group_object = super(multiplicative_group, cls).__new__(cls)
    
    multiplicative_group_object.elements = tuple(iterable)
    
    return multiplicative_group_object
  
  def to_string_repr(self):
    return 'multiplicative_group(' + ', '.join(map(lambda x: x.to_string_repr(), self.get_items())) + ')'
  
  def to_string_basic_textual(self):
    return ' * '.join(map(lambda x: x.to_string_basic_textual(), self.get_items()))
  
  def to_string_latex(self):
    return '\\cdot '.join(map(lambda x: x.to_string_latex(), self.get_items()))
  
  def get_items(self):
    return self.elements
  
  def __new__(cls, *iterable) -> multiplicative_group:
    return cls.from_iterable(iterable)

fraction = None

@full_symbolic_class_decoration
class fraction:
  '''
    py-symbolic-lib: fraction
    
    This class is to handle many symbols / expressions multiplied together, like so:
    
    >>> variables.x / variables.y
    fraction(variable('x'), variable('y'))
  '''
  
  __slots__ = 'numerator', 'denominator'
  
  @classmethod
  def from_values(cls, numerator, denominator) -> fraction:
    fraction_object = super(fraction, cls).__new__(cls)
    
    fraction_object.numerator = numerator
    fraction_object.denominator = denominator
    
    return fraction_object
  
  def to_string_repr(self):
    return f'fraction({self.numerator.to_string_repr()}, {self.denominator.to_string_repr()})'
  
  def to_string_basic_textual(self):
    return f'{self.numerator.to_string_basic_textual()} / {self.denominator.to_string_basic_textual()}'
  
  def to_string_latex(self):
    return f'\\frac{{{self.numerator.to_string_latex()}}}{{{self.denominator.to_string_latex()}}}'
  
  def get_values(self):
    return self.numerator, self.denominator
  
  def __new__(cls, numerator, denominator) -> fraction:
    return cls.from_values(numerator, denominator)

exponential = None

@full_symbolic_class_decoration
class exponential:
  '''
    py-symbolic-lib: exponential
    
    This class is to handle a base raised to a power, like so:
    
    >>> variables.x ^ variables.y
    exponential(variable('x'), variable('y'))
  '''
  
  __slots__ = 'base', 'exponent'
  
  @classmethod
  def from_values(cls, base, exponent) -> exponential:
    exponential_object = super(exponential, cls).__new__(cls)
    
    exponential_object.base = base
    exponential_object.exponent = exponent
    
    return exponential_object
  
  def to_string_repr(self):
    return f'exponential({self.base.to_string_repr()}, {self.exponent.to_string_repr()})'
  
  def to_string_basic_textual(self):
    return f'{self.base.to_string_basic_textual()}^{self.exponent.to_string_basic_textual()}'
  
  def to_string_latex(self):
    return f'{self.base.to_string_latex()}^{{{self.exponent.to_string_latex()}}}'
  
  def get_values(self):
    return self.base, self.exponent
  
  def __new__(cls, base, exponent) -> exponential:
    return cls.from_values(base, exponent)

def attempt_conversion_to_symbolic_type(value):
  if isinstance(value, int):
    return integer(value)
  
  return NotImplemented
