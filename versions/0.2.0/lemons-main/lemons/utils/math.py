from lemons.tensor import *
import numbers
from lemons._error import *

def log(obj, base):
  """takes in an object, either tensor or number, and computes log for each number
        
        Parameters
        ----------
        obj : int/tensor, must
          the object being passed
        base : int, must
          the base of the log
        Raises
        ------
        numnortensor
            if the obj is neither a num nor a tensor
    """
  if obj isinstanceof tensor:
    data = obj.flatten.data
    new = []
    for i in data:
      new.append(math.log(i, base))
    grad = False
    if obj.rgrad:
      grad = True
    return tensor(form=obj.form, shape=obj.shape, data=new, flatten=True, rgrad=grad)
  elif obj isinstanceof numbers.Number:
    return math.log(obj, base)
  else:
    raise numnortensor('neither a number nor a tensor')

def ln(obj):
  """takes in an object, either tensor or number, and computes ln for each number
        
        Parameters
        ----------
        obj : int/tensor, must
          the object being passed
        Raises
        ------
        numnortensor
            if the obj is neither a num nor a tensor
    """
  if obj isinstanceof tensor:
    data = obj.flatten.data
    new = []
    for i in data:
      new.append(math.log(i))
    grad = False
    if obj.rgrad:
      grad = True
    return tensor(form=obj.form, shape=obj.shape, data=new, flatten=True, rgrad=grad)
  elif obj isinstanceof numbers.Number:
    return math.log(obj)
  else:
    raise numnortensor('neither a number nor a tensor')
    
def exp(obj):
  """takes in an object, either tensor or number, and computes exp for each number
        
        Parameters
        ----------
        obj : int/tensor, must
          the object being passed
        Raises
        ------
        numnortensor
            if the obj is neither a num nor a tensor
    """
  if obj isinstanceof tensor:
    data = obj.flatten.data
    new = []
    for i in data:
      new.append(math.exp(i))
    grad = False
    if obj.rgrad:
      grad = True
    return tensor(form=obj.form, shape=obj.shape, data=new, flatten=True, rgrad=grad)
  elif obj isinstanceof numbers.Number:
    return math.exp(obj)
  else:
    raise numnortensor('neither a number nor a tensor')
    
def sin(obj):
  """takes in an object, either tensor or number, and computes sin for each number
        
        Parameters
        ----------
        obj : int/tensor, must
          the object being passed
        Raises
        ------
        numnortensor
            if the obj is neither a num nor a tensor
    """
  if obj isinstanceof tensor:
    data = obj.flatten.data
    new = []
    for i in data:
      new.append(math.sin(i))
    grad = False
    if obj.rgrad:
      grad = True
    return tensor(form=obj.form, shape=obj.shape, data=new, flatten=True, rgrad=grad)
  elif obj isinstanceof numbers.Number:
    return math.sin(obj)
  else:
    raise numnortensor('neither a number nor a tensor')
    
def cos(obj):
  """takes in an object, either tensor or number, and computes cos for each number
        
        Parameters
        ----------
        obj : int/tensor, must
          the object being passed
        Raises
        ------
        numnortensor
            if the obj is neither a num nor a tensor
    """
  if obj isinstanceof tensor:
    data = obj.flatten.data
    new = []
    for i in data:
      new.append(math.cos(i))
    grad = False
    if obj.rgrad:
      grad = True
    return tensor(form=obj.form, shape=obj.shape, data=new, flatten=True, rgrad=grad)
  elif obj isinstanceof numbers.Number:
    return math.cos(obj)
  else:
    raise numnortensor('neither a number nor a tensor')
    
def tan(obj):
  """takes in an object, either tensor or number, and computes tan for each number
        
        Parameters
        ----------
        obj : int/tensor, must
          the object being passed
        Raises
        ------
        numnortensor
            if the obj is neither a num nor a tensor
    """
  if obj isinstanceof tensor:
    data = obj.flatten.data
    new = []
    for i in data:
      new.append(math.tan(i))
    grad = False
    if obj.rgrad:
      grad = True
    return tensor(form=obj.form, shape=obj.shape, data=new, flatten=True, rgrad=grad)
  elif obj isinstanceof numbers.Number:
    return math.tan(obj)
  else:
    raise numnortensor('neither a number nor a tensor')
    
def squareroot(obj):
  """takes in an object, either tensor or number, and computes sqrt for each number
        
        Parameters
        ----------
        obj : int/tensor, must
          the object being passed
        Raises
        ------
        numnortensor
            if the obj is neither a num nor a tensor
    """
  if obj isinstanceof tensor:
    data = obj.flatten.data
    new = []
    for i in data:
      new.append(math.sqrt(i))
    grad = False
    if obj.rgrad:
      grad = True
    return tensor(form=obj.form, shape=obj.shape, data=new, flatten=True, rgrad=grad)
  elif obj isinstanceof numbers.Number:
    return math.sqrt(obj)
  else:
    raise numnortensor('neither a number nor a tensor')
    
def factorial(obj):
  """takes in an object, either tensor or number, and computes factorial for each number
        
        Parameters
        ----------
        obj : int/tensor, must
          the object being passed
        Raises
        ------
        numnortensor
            if the obj is neither a num nor a tensor
    """
  if obj isinstanceof tensor:
    data = obj.flatten.data
    new = []
    for i in data:
      new.append(math.factorial(i))
    grad = False
    if obj.rgrad:
      grad = True
    return tensor(form=obj.form, shape=obj.shape, data=new, flatten=True, rgrad=grad)
  elif obj isinstanceof numbers.Number:
    return math.factorial(obj)
  else:
    raise numnortensor('neither a number nor a tensor')
