from .operators_basic import *

def add_operators_to_class(cls):
  cls.identity = operator_identity
  cls.unary_plus = operator_identity
  cls.pos = operator_identity
  cls.unary_minus = operator_unary_minus
  cls.neg = operator_unary_minus
  
  cls.add = operator_add
  cls.sub = operator_sub
  cls.mul = operator_mul
  cls.div = operator_div
  cls.truediv = operator_div
  cls.pow = operator_pow
  
  #cls.equal = operator_equal
  #cls.eq = operator_equal
  #cls.not_equal = operator_not_equal
  #cls.ne = operator_not_equal
  #cls.greater_than = operator_greater_than
  #cls.gt = operator_greater_than
  #cls.less_than = operator_less_than
  #cls.lt = operator_less_than
  #cls.greater_than_or_equal = operator_greater_than_or_equal
  #cls.ge = operator_greater_than_or_equal
  #cls.less_than_or_equal = operator_less_than_or_equal
  #cls.le = operator_less_than_or_equal
  
  cls.__pos__ = operator_identity
  cls.__neg__ = operator_unary_minus
  
  cls.__add__ = operator_add
  cls.__sub__ = operator_sub
  cls.__mul__ = operator_mul
  cls.__truediv__ = operator_div
  cls.__pow__ = operator_pow
  
  #cls.__eq__ = operator_equal
  #cls.__ne__ = operator_not_equal
  #cls.__gt__ = operator_greater_than
  #cls.__lt__ = operator_less_than
  #cls.__ge__ = operator_greater_than_or_equal
  #cls.__le__ = operator_less_than_or_equal
  
  cls.__radd__ = operator_left_add
  cls.__rsub__ = operator_left_sub
  cls.__rmul__ = operator_left_mul
  cls.__rtruediv__ = operator_left_div
  cls.__rpow__ = operator_left_pow
  
  #cls.__req__ = operator_left_equal
  #cls.__rne__ = operator_left_not_equal
  #cls.__rgt__ = operator_left_greater_than
  #cls.__rlt__ = operator_left_less_than
  #cls.__rge__ = operator_left_greater_than_or_equal
  #cls.__rle__ = operator_left_less_than_or_equal
  
  return cls
