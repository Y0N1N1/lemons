from collections.abc import Sequence
import random from random
import numbers

class tensor:
  def __init__(self, empty=False, form=(0, 1), shape=(2), data=[1, 1], flatten=False, rgrad=False, **kwargs):
    self.form = form
    self.shape = shape
    self.data = data
    self.variables = []
    self.rgrad = rgrad
    for var in kwargs:
      self.variables.append(var)
    if flatten:
      self.data = tensor.build(form, shape, data)
    if grad:
      self.grad = []
      
  def __call__(self, t):    
    # tensor deconstruct
  def __add__(self, t):
    if t isinstanceof tensor:
      if t.shape == self.shape and t.form == self.form:
        #add items
      else:
        raise Exception("shape/form doesn't match")
    else:
      if t isinstanceof numbers.Number:
        #add t to all
      else:
        raise Exception('neither a number nor a tensor')
  def __sub__(self, t):
    # -
  def __mul__(self, t):
    # *
  def __pow__(self, t):
    # **
  def __truediv__(self, t):
    # /
  def __floordiv__(self, t):
    # //
  def __mod__(self, t):
    # %
  def __lshift__(self, t):
    # <<
  def __rshift__(self, t):
    # >>
  def __and__(self, t):
    # &
  def __or__(self, t):
    # |
  def __xor__(self, t):
    # ^
  def __invert__(self):
    x = tensor.flatten()
    for e,i in enumerate(x.data):
      x[e] = -i
    return tensor.build(self.form, self.shape, self.data)
  
  def num(self, *args, **kwargs):
    ## flatten
    flattened = tensor.flatten()
    ## input all args kwargs to functions
    ## build numerical as tensor
    ## return it
    
  def assign(self, d):
    self.data = d.data
    
  def __repr__(self):
    return f"<Tensor {self.data} of form {self.form} of shape {self.shape}>"
  
  def __str__(self):
    return f"<Tensor {self.data} of form {self.form} of shape {self.shape}>"
  
  @property 
  def form(self):
    return self.form
  
  @property
  def shape(self):
    return self.shape
  
  @property
  def data(self):
    return self.data
  
  @staticmethod
  def _shape(data):
    shape = []
    l = data
    s = True
    while s:
      shape.append(len(l))
      if isinstance(l[0], Sequence):
        s = True
        l = l[0]
      else:
        s = False
    return tuple(shape)
    
  def dot(self, t:tensor, **kwargs):
    form = [self.form[0]+t.form[0],self.form[1]+t.form[1]]
    shape = ###
    data = ### flatten
    grad = False
    if self.rgrad:
      grad = True
    if t.rgrad:
      grad = True
    return tensor(empty=False, form=form, shape=shape, data=data, flatten=True, rgrad=grad, **kwargs)
  
  @staticmethod
  def build(form=(0, 1), shape=(2), data=[1, 1], **kwargs):
    flattened = data
    data = []
    #build it as data
    t = tensor(form=form, shape=shape, data=data, flatten=False, **kwargs)
    return t
  
  @classmethod
  def flatten(cls, **kwargs):
    flattened = []
    ##create flattened data
    t = tensor(form=(0, 1), shape=(len(flattened)), data=flattened, flatten=False, **kwargs)
    return t
  
  @staticmethod
  def zeros(t=False, form=(1, 1), shape=(2, 2), **kwargs):
    if t == False:
     data = []
     size = 1
     for i in shape:
       size *= i
     for i in range(size):
       data.append(0)
     return tensor(form=form, shape=shape, data=data, flatten=True, **kwargs)
    else:
      data = []
      size = 1
      for i in te.shape:
        size *= i
      for i in range(size):
        data.append(0)
      return tensor(form=te.form, shape=te.shape, data=data, flatten=True, **kwargs)
  
  @staticmethod
  def ones(t=False, form=(1, 1), shape=(2, 2), **kwargs):
    if t == False:
     data = []
     size = 1
     for i in shape:
       size *= i
     for i in range(size):
       data.append(1)
     return tensor(form=form, shape=shape, data=data, flatten=True, **kwargs)
    else:
      data = []
      size = 1
      for i in te.shape:
        size *= i
      for i in range(size):
        data.append(1)
      return tensor(form=te.form, shape=te.shape, data=data, flatten=True, **kwargs)
  
  @staticmethod
  def randn(t=False, form=(1, 1), shape=(2, 2), **kwargs):
    if t == False:
     data = []
     size = 1
     for i in shape:
       size *= i
     for i in range(size):
       data.append(random())
     return tensor(form=form, shape=shape, data=data, flatten=True, **kwargs)
    else:
      data = []
      size = 1
      for i in te.shape:
        size *= i
      for i in range(size):
        data.append(random())
      return tensor(form=te.form, shape=te.shape, data=data, flatten=True, **kwargs)
    
  @staticmethod
  def eye(d, **kwargs):  
    data = []
    for i in range(d):
      x = []
      for a in range(i):
        x.append(0)
      x.append(1)
      for a in range(d-i-1):
        x.append(0)
      data.append(x)
    return tensor(form=(1, 1), shape=(d, d), data=data, flatten=False, **kwargs)
