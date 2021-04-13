from lemons.tensor import *
import numbers
from lemons._error import *

def log(obj, base):
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
    raise intnortensor('neither a number nor a tensor')

def ln(obj):
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
    raise intnortensor('neither a number nor a tensor')
    
def exp(obj):
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
    raise intnortensor('neither a number nor a tensor')
    
def sin(obj):
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
    raise intnortensor('neither a number nor a tensor')
    
def cos(obj):
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
    raise intnortensor('neither a number nor a tensor')
    
def tan(obj):
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
    raise intnortensor('neither a number nor a tensor')
    
def squareroot(obj):
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
    raise intnortensor('neither a number nor a tensor')
    
def factorial(obj):
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
    raise intnortensor('neither a number nor a tensor')
