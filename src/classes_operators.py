from .classes_common_lib import full_symbolic_class_decoration
from .classes_abstract_base import symbolic_operator

@full_symbolic_class_decoration
class additive_group(symbolic_operator):
  '''
    py-symbolic-lib: additive_group
    
    This class is to handle many symbols / expressions added together, like so:
    
    >>> variables.x + variables.y
    additive_group(variable('x'), variable('y'))
  '''
  
  __slots__ = 'elements',
  
  @classmethod
  def from_iterable(cls, iterable):
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
  
  def get_hashable_form(self):
    return 'additive_group', self.elements
  
  def __new__(cls, *iterable):
    return cls.from_iterable(iterable)

@full_symbolic_class_decoration
class multiplicative_group(symbolic_operator):
  '''
    py-symbolic-lib: multiplicative_group
    
    This class is to handle many symbols / expressions multiplied together, like so:
    
    >>> variables.x * variables.y
    multiplicative_group(variable('x'), variable('y'))
  '''
  
  __slots__ = 'elements',
  
  @classmethod
  def from_iterable(cls, iterable):
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
  
  def get_hashable_form(self):
    return 'multiplicative_group', self.elements
  
  def __new__(cls, *iterable):
    return cls.from_iterable(iterable)

@full_symbolic_class_decoration
class unary_minus(symbolic_operator):
  '''
    py-symbolic-lib: unary_minus
    
    This class is to handle taking the unary minus of an expression, like so:
    
    >>> -variables.x
    unary_minus(variable('x'))
  '''
  
  __slots__ = 'element',
  
  @classmethod
  def from_value(cls, element):
    unary_minus_object = super(unary_minus, cls).__new__(cls)
    
    unary_minus_object.element = element
    
    return unary_minus_object
  
  def to_string_repr(self):
    return f'unary_minus({self.element.to_string_repr()})'
  
  def to_string_basic_textual(self):
    return f'-{self.element.to_string_basic_textual()}'
  
  def to_string_latex(self):
    return f'-{self.element.to_string_latex()}'
  
  def get_element(self):
    return self.element
  
  def get_hashable_form(self):
    return 'unary_minus', self.element
  
  def __new__(cls, element):
    return cls.from_value(element)

@full_symbolic_class_decoration
class fraction(symbolic_operator):
  '''
    py-symbolic-lib: fraction
    
    This class is to handle many symbols / expressions multiplied together, like so:
    
    >>> variables.x / variables.y
    fraction(variable('x'), variable('y'))
  '''
  
  __slots__ = 'numerator', 'denominator'
  
  @classmethod
  def from_values(cls, numerator, denominator):
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
  
  def get_elements(self):
    return self.numerator, self.denominator
  
  def get_hashable_form(self):
    return 'fraction', self.numerator, self.denominator
  
  def __new__(cls, numerator, denominator):
    return cls.from_values(numerator, denominator)

@full_symbolic_class_decoration
class exponential(symbolic_operator):
  '''
    py-symbolic-lib: exponential
    
    This class is to handle a base raised to a power, like so:
    
    >>> variables.x ^ variables.y
    exponential(variable('x'), variable('y'))
  '''
  
  __slots__ = 'base', 'exponent'
  
  @classmethod
  def from_values(cls, base, exponent):
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
  
  def get_elements(self):
    return self.base, self.exponent
  
  def get_hashable_form(self):
    return 'exponential', self.base, self.exponent
  
  def __new__(cls, base, exponent):
    return cls.from_values(base, exponent)
