from .classes_common_lib import full_symbolic_class_decoration
from .classes_abstract_base import symbolic_operator
from . import classes_operator_precedence
from .classes_wrappers import integer

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
  def _raw_from_iterable(cls, iterable):
    additive_group_object = super(additive_group, cls).__new__(cls)
    
    additive_group_object.elements = tuple(iterable)
    
    return additive_group_object
  
  @classmethod
  def from_iterable(cls, iterable):
    return cls.__new__(cls, iterable)
  
  def to_string_repr(self):
    return 'additive_group(' + ', '.join(map(lambda x: x.to_string_repr(), self.get_elements())) + ')'
  
  def to_string_basic(self, do_minus_for_unary_minuses = True, do_minus_for_negative_integers = True):
    string_output = ''
    
    for element in self.get_elements():
      if len(string_output) == 0:
        string_output += element.to_string_basic()
      else:
        if do_minus_for_unary_minuses and isinstance(element, unary_minus):
          string_output += ' - '
          string_output += element.get_element().to_string_basic()
        elif do_minus_for_negative_integers and isinstance(element, integer):
          if element.get_value() < 0:
            string_output += ' - '
            string_output += integer(-element.get_value()).to_string_basic()
          else:
            string_output += ' + '
            string_output += element.to_string_basic()
        else:
          string_output += ' + '
          string_output += element.to_string_basic()
    
    return string_output
  
  def to_string_compact(self, do_minus_for_unary_minuses = True, do_minus_for_negative_integers = True):
    string_output = ''
    
    for element in self.get_elements():
      if len(string_output) == 0:
        string_output += element.to_string_compact()
      else:
        if do_minus_for_unary_minuses and isinstance(element, unary_minus):
          string_output += '-'
          string_output += element.get_element().to_string_compact()
        elif do_minus_for_negative_integers and isinstance(element, integer):
          if element.get_value() < 0:
            string_output += '-'
            string_output += integer(-element.get_value()).to_string_compact()
          else:
            string_output += '+'
            string_output += element.to_string_compact()
        else:
          string_output += '+'
          string_output += element.to_string_compact()
    
    return string_output
  
  def to_string_latex(self, do_minus_for_unary_minuses = True, do_minus_for_negative_integers = True):
    string_output = ''
    
    for element in self.get_elements():
      if len(string_output) == 0:
        string_output += element.to_string_latex()
      else:
        if do_minus_for_unary_minuses and isinstance(element, unary_minus):
          string_output += '-'
          string_output += element.get_element().to_string_latex()
        elif do_minus_for_negative_integers and isinstance(element, integer):
          if element.get_value() < 0:
            string_output += '-'
            string_output += integer(-element.get_value()).to_string_latex()
          else:
            string_output += '+'
            string_output += element.to_string_latex()
        else:
          string_output += '+'
          string_output += element.to_string_latex()
    
    return string_output
  
  def get_elements(self):
    return self.elements
  
  def get_hashable_form(self):
    return 'additive_group', tuple(map(lambda x: x.get_hashable_form(), self.get_elements()))
  
  def __new__(cls, *iterable):
    return cls._raw_from_iterable(iterable)

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
  def _raw_from_iterable(cls, iterable):
    multiplicative_group_object = super(multiplicative_group, cls).__new__(cls)
    
    multiplicative_group_object.elements = tuple(iterable)
    
    return multiplicative_group_object
  
  @classmethod
  def from_iterable(cls, iterable):
    return cls.__new__(cls, iterable)
  
  def to_string_repr(self):
    return 'multiplicative_group(' + ', '.join(map(lambda x: x.to_string_repr(), self.get_elements())) + ')'
  
  def to_string_basic(self):
    return ' * '.join(map(
      lambda x: classes_operator_precedence._parenthesis_if_lower_precedence(self, x, x.to_string_basic()),
      self.get_elements()
    ))
  
  def to_string_compact(self):
    return '*'.join(map(
      lambda x: classes_operator_precedence._parenthesis_if_lower_precedence(self, x, x.to_string_compact()),
      self.get_elements()
    ))
  
  def to_string_latex(self):
    return '\\cdot '.join(map(
      lambda x: classes_operator_precedence._parenthesis_if_lower_precedence(self, x, x.to_string_latex(), latex = True),
      self.get_elements()
    ))
  
  def get_elements(self):
    return self.elements
  
  def get_hashable_form(self):
    return 'multiplicative_group', tuple(map(lambda x: x.get_hashable_form(), self.get_elements()))
  
  def __new__(cls, *iterable):
    return cls._raw_from_iterable(iterable)

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
  def _raw_from_value(cls, element):
    unary_minus_object = super(unary_minus, cls).__new__(cls)
    
    unary_minus_object.element = element
    
    return unary_minus_object
  
  @classmethod
  def from_value(cls, element):
    return cls.__new__(cls, element)
  
  def to_string_repr(self):
    return f'unary_minus({self.element.to_string_repr()})'
  
  def to_string_basic(self):
    return f'-{classes_operator_precedence._parenthesis_if_lower_precedence(self, self.element, self.element.to_string_basic())}'
  
  def to_string_compact(self):
    return f'-{classes_operator_precedence._parenthesis_if_lower_precedence(self, self.element, self.element.to_string_compact())}'
  
  def to_string_latex(self):
    return f'-{classes_operator_precedence._parenthesis_if_lower_precedence(self, self.element, self.element.to_string_latex(), latex = True)}'
  
  def get_element(self):
    return self.element
  
  def get_hashable_form(self):
    return 'unary_minus', self.element.get_hashable_form()
  
  def __new__(cls, element):
    return cls._raw_from_value(element)

@full_symbolic_class_decoration
class fraction(symbolic_operator):
  '''
    py-symbolic-lib: fraction
    
    This class is to handle a numerator divided by a denominator, like so:
    
    >>> variables.x / variables.y
    fraction(variable('x'), variable('y'))
  '''
  
  __slots__ = 'numerator', 'denominator'
  
  @classmethod
  def _raw_from_values(cls, numerator, denominator):
    fraction_object = super(fraction, cls).__new__(cls)
    
    fraction_object.numerator = numerator
    fraction_object.denominator = denominator
    
    return fraction_object
  
  @classmethod
  def from_values(cls, numerator, denominator):
    return cls.__new__(cls, numerator, denominator)
  
  def to_string_repr(self):
    return f'fraction({self.numerator.to_string_repr()}, {self.denominator.to_string_repr()})'
  
  def to_string_basic(self):
    return classes_operator_precedence._parenthesis_if_lower_precedence(self, self.numerator, self.numerator.to_string_basic()) + \
      ' / ' + \
      classes_operator_precedence._parenthesis_if_lower_precedence(self, self.denominator, self.denominator.to_string_basic())
  
  def to_string_compact(self):
    return classes_operator_precedence._parenthesis_if_lower_precedence(self, self.numerator, self.numerator.to_string_compact()) + \
      '/' + \
      classes_operator_precedence._parenthesis_if_lower_precedence(self, self.denominator, self.denominator.to_string_compact())
  
  def to_string_latex(self):
    return f'\\frac{{{classes_operator_precedence._parenthesis_if_lower_precedence(self, self.numerator, self.numerator.to_string_latex(), latex = True)}}}' + \
    f'{{{classes_operator_precedence._parenthesis_if_lower_precedence(self, self.denominator, self.denominator.to_string_latex(), latex = True)}}}'
  
  def get_elements(self):
    return self.numerator, self.denominator
  
  def get_hashable_form(self):
    return 'fraction', self.numerator.get_hashable_form(), self.denominator.get_hashable_form()
  
  def __new__(cls, numerator, denominator):
    return cls._raw_from_values(numerator, denominator)

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
  def _raw_from_values(cls, base, exponent):
    exponential_object = super(exponential, cls).__new__(cls)
    
    exponential_object.base = base
    exponential_object.exponent = exponent
    
    return exponential_object
  
  @classmethod
  def from_values(cls, base, exponent):
    return cls.__new__(cls, base, exponent)
  
  def to_string_repr(self):
    return f'exponential({self.base.to_string_repr()}, {self.exponent.to_string_repr()})'
  
  def to_string_basic(self):
    return classes_operator_precedence._parenthesis_if_lower_precedence(self, self.base, self.base.to_string_basic()) + \
    '^' + \
    classes_operator_precedence._parenthesis_if_lower_precedence(self, self.exponent, self.exponent.to_string_basic(), exponential_exponent = True)
  
  def to_string_compact(self):
    return classes_operator_precedence._parenthesis_if_lower_precedence(self, self.base, self.base.to_string_compact()) + \
    '^' + \
    classes_operator_precedence._parenthesis_if_lower_precedence(self, self.exponent, self.exponent.to_string_compact(), exponential_exponent = True)
  
  def to_string_latex(self):
    return classes_operator_precedence._parenthesis_if_lower_precedence(self, self.base, self.base.to_string_latex(), latex = True) + \
    '^' + \
    f'{{{classes_operator_precedence._parenthesis_if_lower_precedence(self, self.exponent, self.exponent.to_string_latex(), latex = True, exponential_exponent = True)}}}'
  
  def get_elements(self):
    return self.base, self.exponent
  
  def get_hashable_form(self):
    return 'exponential', self.base.get_hashable_form(), self.exponent.get_hashable_form()
  
  def __new__(cls, base, exponent):
    return cls._raw_from_values(base, exponent)
