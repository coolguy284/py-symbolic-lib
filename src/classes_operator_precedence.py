from . import classes

def _make_dict_with_indexes_as_values(*input_args):
  output_dict = {}
  
  for i in range(len(input_args)):
    output_dict[input_args[i]] = len(input_args) - i
  
  return output_dict

_operator_precedence_exponential_base_or_anything_else = None
_operator_precedence_exponential_exponent = None

def _classes_operator_precedence_make_lookup_tables():
  global _operator_precedence_exponential_base_or_anything_else, _operator_precedence_exponential_exponent
  
  _operator_precedence_exponential_base_or_anything_else = _make_dict_with_indexes_as_values(
    classes.integer,
    classes.variable,
    classes.exponential,
    classes.unary_minus,
    classes.fraction,
    classes.multiplicative_group,
    classes.additive_group,
  )

  _operator_precedence_exponential_exponent = _make_dict_with_indexes_as_values(
    classes.integer,
    classes.variable,
    classes.unary_minus,
    classes.exponential,
    classes.fraction,
    classes.multiplicative_group,
    classes.additive_group,
  )

_operator_precedence_exponential_base_add_parens_for_exponential = True
_operator_precedence_exponential_exponent_add_parens_for_exponential = False

def _parenthesis_if_lower_precedence_should_do_parenthesis(object_outer, object_inner, exponential_exponent = False):
  if _operator_precedence_exponential_base_or_anything_else is None:
    _classes_operator_precedence_make_lookup_tables()
  
  if type(object_outer) is classes.exponential and type(object_inner) is classes.exponential:
    if exponential_exponent:
      return _operator_precedence_exponential_exponent_add_parens_for_exponential
    else:
      return _operator_precedence_exponential_base_add_parens_for_exponential
  
  if exponential_exponent:
    outer_precedence = _operator_precedence_exponential_exponent[type(object_outer)]
    inner_precedence = _operator_precedence_exponential_exponent[type(object_inner)]
  else:
    outer_precedence = _operator_precedence_exponential_base_or_anything_else[type(object_outer)]
    inner_precedence = _operator_precedence_exponential_base_or_anything_else[type(object_inner)]
  
  return outer_precedence > inner_precedence

def _parenthesis_if_lower_precedence(object_outer, object_inner, base_string, latex = False, exponential_exponent = False):
  should_add_parens = _parenthesis_if_lower_precedence_should_do_parenthesis(object_outer, object_inner, exponential_exponent)
  
  if should_add_parens:
    if latex:
      return f'\\left({base_string}\\right)'
    else:
      return f'({base_string})'
  else:
    return base_string
