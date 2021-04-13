from collections.abc import Sequence
import random from random
import numbers
from lemons._error import *

class tensor:
  """
    A class used to represent a mathematical tensor

    the class provides useful functions for both the mathematical representation of tensors
    (following the covariant contravariant forms)
    and a way to treat tensors in the computer science form
    (following the shape properties)

    Attributes
    ----------
    form : tuple, optional
      the mathematical form of the tensor, always two numbers
    shape : tuple, optional
      the computer science representation of a tensor as a multidimensional array
    data : list, optional
      the tensor itself, containing all the data, may be inputed flattened if flatten=True
    variables : list, optional
      an array of variables/functions inserted through **kwargs, called through variable()
    rgrad : bool, optional
      if the tensor requires grad and this if history should be saved
      
    Methods
    -------
    __init__(empty=False, form=(0, 1), shape=(2), data=[1, 1], flatten=False, rgrad=False, **kwargs)
        takes in form, shape and data to build the basis
    __call__()
  """
  def __init__(self, empty=False, form=(0, 1), shape=(2), data=[1, 1], flatten=False, rgrad=False, **kwargs):
    """takes in form, shape and data to build the basis

        if empty isn't set to true, the tensor will not be empty, if form, shape and data are not provided
        the tensor will be a (1, 1) vector. If flatten is true, the tensor will be passed as flattened and
        will be constructed artificially, if rgrad is set to true, a history for the grad will be recorded
        kwargs are other variables/functions stored in a list called variables.

        Parameters
        ----------
        form : tuple, optional
          the mathematical form of the tensor, always two numbers
        shape : tuple, optional
          the computer science representation of a tensor as a multidimensional array
        data : list, optional
          the tensor itself, containing all the data, may be inputed flattened if flatten=True
        kwargs : dict, optional
          an array of variables/functions inserted through **kwargs, called through variable()
        rgrad : bool, optional
          if the tensor requires grad and this if history should be saved

        Raises
        ------
        WrongShape
            If no sound is set for the animal or passed in as a
            parameter.
    """
    
    self.form = form
    self.shape = shape
    self.data = data
    self.variables = []
    self.rgrad = rgrad
    for var in kwargs:
      self.variables.append(var)
    if flatten:
      self.data = tensor.build(form, shape, data).data
    if grad:
      self.grad = []
    if shape != tensor._shape(self.data):
      raise Nshape("tensor with wrong shape")
    
      
  def __call__(self, t:tensor, selfi, ti, **kwargs):    
    """takes in another tensor and indexes to create a new tensor

        Parameters
        ----------
        t : tensor, optional
          the tensor being dotted to 
        selfi : tuple, optional
          the indexes of the self tensor, arranged as ((),())
        ti : tuple, optional
          the indexes of the tensor being do, arranged as ((),())
        kwargs : dict, optional
          an array of variables/functions inserted through **kwargs, called through variable()

        Raises
        ------
        
    """
    
  def __add__(self, t):
    # +
    if t isinstanceof tensor:
      if t.shape == self.shape and t.form == self.form:
        data = self.flatten
        tdata = t.flatten
        new = []
        for e, i in enumerate(data.data):
          x = i + tdata.data[e]
          new.append(x)
        data = tensor.build(form=self.form, shape=self.shape, data=new)
        data.variables = self.variables
        return data
      else:
        raise shapeform("shape/form doesn't match")
    else:
      if t isinstanceof numbers.Number:
        data = self.flatten
        for e,i in enumerate(data.data):
          data.data[e] = i + t 
        data = tensor.build(form=self.form, shape=self.shape, data=data)
        data.variables = self.variables
        return data
      else:
        raise intnortensor('neither a number nor a tensor')
  
  def __sub__(self, t):
    # -
    if t isinstanceof tensor:
      if t.shape == self.shape and t.form == self.form:
        data = self.flatten
        tdata = t.flatten
        new = []
        for e, i in enumerate(data.data):
          x = i - tdata.data[e]
          new.append(x)
        data = tensor.build(form=self.form, shape=self.shape, data=new)
        data.variables = self.variables
        return data
      else:
        raise shapeform("shape/form doesn't match")
    else:
      if t isinstanceof numbers.Number:
        data = self.flatten
        for e,i in enumerate(data.data):
          data.data[e] = i - t 
        data = tensor.build(form=self.form, shape=self.shape, data=data)
        data.variables = self.variables
        return data
      else:
        raise intnortensor('neither a number nor a tensor')
  
  def __mul__(self, t):
    # *
    if t isinstanceof tensor:
      if t.shape == self.shape and t.form == self.form:
        data = self.flatten
        tdata = t.flatten
        new = []
        for e, i in enumerate(data.data):
          x = i * tdata.data[e]
          new.append(x)
        data = tensor.build(form=self.form, shape=self.shape, data=new)
        data.variables = self.variables
        return data
      else:
        raise shapeform("shape/form doesn't match")
    else:
      if t isinstanceof numbers.Number:
        data = self.flatten
        for e,i in enumerate(data.data):
          data.data[e] = i * t 
        data = tensor.build(form=self.form, shape=self.shape, data=data)
        data.variables = self.variables
        return data
      else:
        raise intnortensor('neither a number nor a tensor')
  
  def __pow__(self, t):
    # **
    if t isinstanceof tensor:
      if t.shape == self.shape and t.form == self.form:
        data = self.flatten
        tdata = t.flatten
        new = []
        for e, i in enumerate(data.data):
          x = i ** tdata.data[e]
          new.append(x)
        data = tensor.build(form=self.form, shape=self.shape, data=new)
        data.variables = self.variables
        return data
      else:
        raise shapeform("shape/form doesn't match")
    else:
      if t isinstanceof numbers.Number:
        data = self.flatten
        for e,i in enumerate(data.data):
          data.data[e] = i ** t 
        data = tensor.build(form=self.form, shape=self.shape, data=data)
        data.variables = self.variables
        return data
      else:
        raise intnortensor('neither a number nor a tensor')
  
  def __truediv__(self, t):
    # /
    if t isinstanceof tensor:
      if t.shape == self.shape and t.form == self.form:
        data = self.flatten
        tdata = t.flatten
        new = []
        for e, i in enumerate(data.data):
          x = i / tdata.data[e]
          new.append(x)
        data = tensor.build(form=self.form, shape=self.shape, data=new)
        data.variables = self.variables
        return data
      else:
        raise shapeform("shape/form doesn't match")
    else:
      if t isinstanceof numbers.Number:
        data = self.flatten
        for e,i in enumerate(data.data):
          data.data[e] = i / t 
        data = tensor.build(form=self.form, shape=self.shape, data=data)
        data.variables = self.variables
        return data
      else:
        raise intnortensor('neither a number nor a tensor')
  
  def __floordiv__(self, t):
    # //
    if t isinstanceof tensor:
      if t.shape == self.shape and t.form == self.form:
        data = self.flatten
        tdata = t.flatten
        new = []
        for e, i in enumerate(data.data):
          x = i // tdata.data[e]
          new.append(x)
        data = tensor.build(form=self.form, shape=self.shape, data=new)
        data.variables = self.variables
        return data
      else:
        raise shapeform("shape/form doesn't match")
    else:
      if t isinstanceof numbers.Number:
        data = self.flatten
        for e,i in enumerate(data.data):
          data.data[e] = i // t 
        data = tensor.build(form=self.form, shape=self.shape, data=data)
        data.variables = self.variables
        return data
      else:
        raise intnortensor('neither a number nor a tensor')
  
  def __mod__(self, t):
    # %
    if t isinstanceof tensor:
      if t.shape == self.shape and t.form == self.form:
        data = self.flatten
        tdata = t.flatten
        new = []
        for e, i in enumerate(data.data):
          x = i % tdata.data[e]
          new.append(x)
        data = tensor.build(form=self.form, shape=self.shape, data=new)
        data.variables = self.variables
        return data
      else:
        raise shapeform("shape/form doesn't match")
    else:
      if t isinstanceof numbers.Number:
        data = self.flatten
        for e,i in enumerate(data.data):
          data.data[e] = i % t 
        data = tensor.build(form=self.form, shape=self.shape, data=data)
        data.variables = self.variables
        return data
      else:
        raise intnortensor('neither a number nor a tensor')
  
  def __lshift__(self, t):
    # <<
    if t isinstanceof tensor:
      if t.shape == self.shape and t.form == self.form:
        data = self.flatten
        tdata = t.flatten
        new = []
        for e, i in enumerate(data.data):
          x = i << tdata.data[e]
          new.append(x)
        data = tensor.build(form=self.form, shape=self.shape, data=new)
        data.variables = self.variables
        return data
      else:
        raise shapeform("shape/form doesn't match")
    else:
      if t isinstanceof numbers.Number:
        data = self.flatten
        for e,i in enumerate(data.data):
          data.data[e] = i << t 
        data = tensor.build(form=self.form, shape=self.shape, data=data)
        data.variables = self.variables
        return data
      else:
        raise intnortensor('neither a number nor a tensor')
  
  def __rshift__(self, t):
    # >>
    if t isinstanceof tensor:
      if t.shape == self.shape and t.form == self.form:
        data = self.flatten
        tdata = t.flatten
        new = []
        for e, i in enumerate(data.data):
          x = i >> tdata.data[e]
          new.append(x)
        data = tensor.build(form=self.form, shape=self.shape, data=new)
        data.variables = self.variables
        return data
      else:
        raise shapeform("shape/form doesn't match")
    else:
      if t isinstanceof numbers.Number:
        data = self.flatten
        for e,i in enumerate(data.data):
          data.data[e] = i >> t 
        data = tensor.build(form=self.form, shape=self.shape, data=data)
        data.variables = self.variables
        return data
      else:
        raise intnortensor('neither a number nor a tensor')
  
  def __and__(self, t):
    # &
    if t isinstanceof tensor:
      if t.shape == self.shape and t.form == self.form:
        data = self.flatten
        tdata = t.flatten
        new = []
        for e, i in enumerate(data.data):
          x = i & tdata.data[e]
          new.append(x)
        data = tensor.build(form=self.form, shape=self.shape, data=new)
        data.variables = self.variables
        return data
      else:
        raise shapeform("shape/form doesn't match")
    else:
      if t isinstanceof numbers.Number:
        data = self.flatten
        for e,i in enumerate(data.data):
          data.data[e] = i & t 
        data = tensor.build(form=self.form, shape=self.shape, data=data)
        data.variables = self.variables
        return data
      else:
        raise intnortensor('neither a number nor a tensor')
  
  def __or__(self, t):
    # |
    if t isinstanceof tensor:
      if t.shape == self.shape and t.form == self.form:
        data = self.flatten
        tdata = t.flatten
        new = []
        for e, i in enumerate(data.data):
          x = i | tdata.data[e]
          new.append(x)
        data = tensor.build(form=self.form, shape=self.shape, data=new)
        data.variables = self.variables
        return data
      else:
        raise shapeform("shape/form doesn't match")
    else:
      if t isinstanceof numbers.Number:
        data = self.flatten
        for e,i in enumerate(data.data):
          data.data[e] = i | t 
        data = tensor.build(form=self.form, shape=self.shape, data=data)
        data.variables = self.variables
        return data
      else:
        raise intnortensor('neither a number nor a tensor')
  
  def __xor__(self, t):
    # ^
    if t isinstanceof tensor:
      if t.shape == self.shape and t.form == self.form:
        data = self.flatten
        tdata = t.flatten
        new = []
        for e, i in enumerate(data.data):
          x = i ^ tdata.data[e]
          new.append(x)
        data = tensor.build(form=self.form, shape=self.shape, data=new)
        data.variables = self.variables
        return data
      else:
        raise shapeform("shape/form doesn't match")
    else:
      if t isinstanceof numbers.Number:
        data = self.flatten
        for e,i in enumerate(data.data):
          data.data[e] = i ^ t 
        data = tensor.build(form=self.form, shape=self.shape, data=data)
        data.variables = self.variables
        return data
      else:
        raise intnortensor('neither a number nor a tensor')
  
  def __invert__(self):
    x = tensor.flatten()
    for e,i in enumerate(x.data):
      x[e] = -i
    return tensor.build(self.form, self.shape, self.data)
  
  def num(self, *args, **kwargs):
    ## flatten
    flattened = self.flatten
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
  
  @property
  def flatten(self):
    flattened = []
    ##create flattened data
    t = tensor(form=(0, 1), shape=(len(flattened)), data=flattened, flatten=False)
    t.variables = self.variables
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

  @staticmethod
  def const(form=(0, 1), shape=(2), const=1, **kwargs):
    n = 1
    for i in shape:
      n *= i
    data = []
    for i in range(n):
      data.append(const)
    return tensor(form=form, shape=shape, data=data, flatten=True, **kwargs)
  
  @staticmethod
  def core(form=(0, 1), shape=(2), data=1, **kwargs):
    
    
  def sum(self):
    s = 0
    x = self.flatten
    for i in x.data:
      s += i
    return s
  
  
