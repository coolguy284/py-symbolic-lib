from weakref import WeakValueDictionary

from .operators import add_operators_to_class

def full_symbolic_class_decoration(cls):
  # add operators to class
  
  cls = add_operators_to_class(cls)
  
  # check for required methods
  
  if not hasattr(cls, 'to_string_repr'):
    raise Exception(f'to_string_repr not found on class {cls.__name__}')
  
  if not hasattr(cls, 'to_string_basic'):
    raise Exception(f'to_string_basic not found on class {cls.__name__}')
  
  if not hasattr(cls, 'to_string_compact'):
    raise Exception(f'to_string_compact not found on class {cls.__name__}')
  
  if not hasattr(cls, 'to_string_latex'):
    raise Exception(f'to_string_latex not found on class {cls.__name__}')
    
  if not hasattr(cls, 'get_hashable_form'):
    raise Exception(f'get_hashable_form not found on class {cls.__name__}')
  
  # bind some dunder methods
  
  cls.__repr__ = cls.to_string_repr
  cls.__str__ = cls.to_string_basic
  
  def cls_hash(self):
    return hash(self.get_hashable_form())
  
  cls.hash = cls_hash
  cls.__hash__ = cls_hash
    
  # implement memoization
  
  cls._instance_dict = WeakValueDictionary()
  
  cls_original_new = cls.__new__
  
  def cls_new_new(cls, *args):
    new_instance = cls_original_new(cls, *args)
    
    hashable_key = new_instance.get_hashable_form()
    
    if hashable_key in cls._instance_dict:
      return cls._instance_dict[hashable_key]
    else:
      cls._instance_dict[hashable_key] = new_instance
      
      return new_instance
  
  cls.__new__ = cls_new_new
  
  return cls
