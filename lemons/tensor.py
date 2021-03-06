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
    __init__(self, empty=False, form=(0, 1), shape=(2), data=[1, 1], flatten=False, rgrad=False, **kwargs)
        takes in form, shape and data to build the basis
    __call__(self, t:tensor, selfi, ti, **kwargs)
        takes in another tensor and indexes to create a new tensor
    __add__(self, t)
        + tensors or + the self tensor with number
    __sub__(self, t)
        - tensors or - the self tensor with number
    __mul__(self, t)
        * tensors or * the self tensor with number
    __pow__(self, t)
        ** tensors or ** the self tensor with number
    __truediv__(self, t)
        / tensors or / the self tensor with number
    __floordiv__(self, t)
        // tensors or // the self tensor with number
    __mod__(self, t)
        % tensors or % the self tensor with number
    __lshift__(self, t)
        << tensors or << the self tensor with number
    __rshift__(self, t)
        >> tensors or >> the self tensor with number
    __and__(self, t)
        & tensors or & the self tensor with number
    __or__(self, t)
        | tensors or | the self tensor with number
    __xor__(self, t)
        ^ tensors or ^ the self tensor with number
    __invert__(self)
        inverts self tensor negative   
    __repr__(self)
        returns the printable version of the tensor
    __str__(self)
        returns the printable version of the tensor
    num()
        
    assign() 
        
    rank() 
        
    form()
        
    shape()
        
    data()
        
    variables() 
        
    formtranspose() 
        
    shapelen()
        
    shapetranspose() 
        
    transpose()
        
    formdot()
        
    shapedot()
        
    dot()
        
    build() 
        
    flatten() 
        
    zeros()
        
    ones()
        
    randn()
        
    eye()
        
    const()
        
    core()
        
    sum()
        
    pretty()
        
    _shape()
        
    _shapelen() 
        
    _rank()
        
    transform(self, jacobian, inversejacobian)
        transforms tensor
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
        notshape
            if the shape doesn't match with the tensor's data
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
    if rgrad:
      self.grad = []
    if shape != tensor._shape(self.data):
      raise notshape("tensor with wrong shape")
    
      
  def __call__(self, *args, **kwargs):    
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
        Returns
        ------
        tensor
          a tensor of the resulting equation
    """
    
  def __add__(self, t):
    """+ tensors or + the self tensor with number

        Parameters
        ----------
        t : number/tensor, optional
          the tensor/number being + to 

        Raises
        ------
        shapeform
          if the shapes of both tensors don't match
        numnortensor
        if the input is neither a number nor a tensor
        
        Returns
        ------
        tensor
          a tensor of the resulting opperation
        
    """
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
        raise numnortensor('neither a number nor a tensor')
  
  def __sub__(self, t):
    """- tensors or - the self tensor with number

        Parameters
        ----------
        t : number/tensor, optional
          the tensor/number being - to 

        Raises
        ------
        shapeform
          if the shapes of both tensors don't match
        numnortensor
        if the input is neither a number nor a tensor
        
        Returns
        ------
        tensor
          a tensor of the resulting opperation
        
    """
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
        raise numnortensor('neither a number nor a tensor')
  
  def __mul__(self, t):
    """* tensors or * the self tensor with number

        Parameters
        ----------
        t : number/tensor, optional
          the tensor/number being * to 

        Raises
        ------
        shapeform
          if the shapes of both tensors don't match
        numnortensor
        if the input is neither a number nor a tensor
        
        Returns
        ------
        tensor
          a tensor of the resulting opperation
    """
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
        raise numnortensor('neither a number nor a tensor')
  
  def __pow__(self, t):
    """** tensors or ** the self tensor with number

        Parameters
        ----------
        t : number/tensor, optional
          the tensor/number being ** to 

        Raises
        ------
        shapeform
          if the shapes of both tensors don't match
        numnortensor
        if the input is neither a number nor a tensor
        
        Returns
        ------
        tensor
          a tensor of the resulting opperation
        
    """
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
        raise numnortensor('neither a number nor a tensor')
 
  def __truediv__(self, t):
    """/ tensors or / the self tensor with number

        Parameters
        ----------
        t : number/tensor, optional
          the tensor/number being / to 

        Raises
        ------
        shapeform
          if the shapes of both tensors don't match
        numnortensor
        if the input is neither a number nor a tensor
        
        Returns
        ------
        tensor
          a tensor of the resulting opperation
        
    """
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
        raise numnortensor('neither a number nor a tensor')
  
  def __floordiv__(self, t):
    """// tensors or // the self tensor with number

        Parameters
        ----------
        t : number/tensor, optional
          the tensor/number being // to 

        Raises
        ------
        shapeform
          if the shapes of both tensors don't match
        numnortensor
        if the input is neither a number nor a tensor
        
        Returns
        ------
        tensor
          a tensor of the resulting opperation
        
    """
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
        raise numnortensor('neither a number nor a tensor')
  
  def __mod__(self, t):
    """% tensors or % the self tensor with number

        Parameters
        ----------
        t : number/tensor, optional
          the tensor/number being % to 

        Raises
        ------
        shapeform
          if the shapes of both tensors don't match
        numnortensor
        if the input is neither a number nor a tensor
        
        Returns
        ------
        tensor
          a tensor of the resulting opperation
        
    """
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
        raise numnortensor('neither a number nor a tensor')
  
  def __lshift__(self, t):
    """<< tensors or << the self tensor with number

        Parameters
        ----------
        t : number/tensor, optional
          the tensor/number being << to 

        Raises
        ------
        shapeform
          if the shapes of both tensors don't match
        numnortensor
        if the input is neither a number nor a tensor
        
        Returns
        ------
        tensor
          a tensor of the resulting opperation
        
    """
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
        raise numnortensor('neither a number nor a tensor')
  
  def __rshift__(self, t):
    """>> tensors or >> the self tensor with number

        Parameters
        ----------
        t : number/tensor, optional
          the tensor/number being >> to 

        Raises
        ------
        shapeform
          if the shapes of both tensors don't match
        numnortensor
          if the input is neither a number nor a tensor
        
        Returns
        ------
        tensor
          a tensor of the resulting opperation
        
    """
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
        raise numnortensor('neither a number nor a tensor')
  
  def __and__(self, t):
    """& tensors or & the self tensor with number

        Parameters
        ----------
        t : number/tensor, optional
          the tensor/number being & to 

        Raises
        ------
        shapeform
          if the shapes of both tensors don't match
        numnortensor
        if the input is neither a number nor a tensor
        
        Returns
        ------
        tensor
          a tensor of the resulting opperation
        
    """
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
        raise numnortensor('neither a number nor a tensor')
  
  def __or__(self, t):
    """| tensors or | the self tensor with number

        Parameters
        ----------
        t : number/tensor, optional
          the tensor/number being | to 

        Raises
        ------
        shapeform
          if the shapes of both tensors don't match
        numnortensor
        if the input is neither a number nor a tensor
        
        Returns
        ------
        tensor
          a tensor of the resulting opperation
        
    """
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
        raise numnortensor('neither a number nor a tensor')
  
  def __xor__(self, t):
    """^ tensors or ^ the self tensor with number

        Parameters
        ----------
        t : number/tensor, optional
          the tensor/number being ^ to 

        Raises
        ------
        shapeform
          if the shapes of both tensors don't match
        numnortensor
        if the input is neither a number nor a tensor
        
        Returns
        ------
        tensor
          a tensor of the resulting opperation
        
    """
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
        raise numnortensor('neither a number nor a tensor')
  
  def __invert__(self):
    """inverts self tensor negative    
        
        Returns
        ------
        tensor
          a tensor of the resulting opperation 
    """
    x = tensor.flatten()
    for e,i in enumerate(x.data):
      x[e] = -i
    return tensor.build(self.form, self.shape, self.data)
  
  def num(self, *args, **kwargs):
    """returns the numeric version of the tensor, if the tensor is made up of functions
        
        Returns
        ------
        tensor
          returns the numeric version of the tensor, if the tensor is made up of functions
    """
    ## flatten
    flattened = self.flatten
    ## input all args kwargs to functions
    ## build numerical as tensor
    ## return it
    
  def assign(self, empty=False, form=(0, 1), shape=(2), data=[1, 1], flatten=False, rgrad=False, **kwargs):
    """assigns a whole new tensor to the tensor
        
        Returns
        ------
        tensor
          zxxigns a whole new tensor to the tensor
    """
    self.form = form
    self.shape = shape
    self.data = data
    self.rgrad = rgrad
    for var in kwargs:
      self.variables.append(var)
    if flatten:
      self.data = tensor.build(form, shape, data).data
    if rgrad:
      self.grad = []
    if shape != tensor._shape(self.data):
      raise notshape("tensor with wrong shape")
    
  def __repr__(self):
    """returns the printable version of the tensor
        
        Returns
        ------
        tensor
          returns the printable version of the tensor
    """
    return f"<Tensor {self.data} of form {self.form} of shape {self.shape}>"
  
  def __str__(self):
    """returns the printable version of the tensor
        
        Returns
        ------
        tensor
          returns the printable version of the tensor
    """
    return f"<Tensor {self.data} of form {self.form} of shape {self.shape}>"
  
  @staticmethod
  def _rank(shape):
    """returns the rank of the inputted shape
        
        Returns
        ------
        number
          returns the rank of the inputted shape
    """
    return len(shape)
  
  @property
  def rank(self):
    """returns the rank of the tensor
        
        Returns
        ------
        number
          returns the rank of the tensor
    """
    return len(self.shape)
  
  @property 
  def form(self):
    """returns the form of the tensor
        
        Returns
        ------
        tuple
          returns the form of the tensor
    """
    return self.form
  
  @property
  def shape(self):
    """returns the shape of the tensor
        
        Returns
        ------
        tuple
          returns the shape of the tensor
    """
    return self.shape
  
  @property
  def data(self):
    """returns the data of the tensor
        
        Returns
        ------
        list
          returns the data of the tensor
    """
    return self.data
  
  @property
  def variables(self):
    """returns the variables of the tensor
        
        Returns
        ------
        list
          returns the variables of the tensor
    """
    return self.variables
 
  @staticmethod
  def formtranspose(form):
    """returns the transpose of the inputted form
        
        Returns
        ------
        tuple
          returns the transpose of the inputted form
    """
    return (form[1], form[0])
  
  @staticmethd
  def _shapelen(shape):
    """returns the multiplication of all items in the shape, this gives the total number of numbers in the tensor
        
        Returns
        ------
        tensor
          returns the multiplication of all items in the shape, this gives the total number of numbers in the tensor
    """
    x = 1
    for i in shape:
      x *= i
    return x
  
  @property
  def shapelen(self):
    """returns the shapelen of the tensor (length of flattened tensor)
        
        Returns
        ------
        number
          returns the shapelen of the tensor
    """
    x = 1
    for i in self.shape:
      x *= i
    return x
  
  @staticmethod
  def shapetranspose(shape):
    """returns the transpose of the inputted shape
        
        Returns
        ------
        tuple
          returns the transpose of the inputted shape
    """
    new = list(self.shape)
    return tuple(new.reverse())
  
  def reshape(self, newshape, newform):
    """returns the self tensor but with a new shape
        
        Returns
        ------
        tensor
          returns the self tensor but with a new shape
    """
    old = tensor.shapelen()
    new = tensor._shapelen(newshape)
    if old == new:
      if newform[1]+newform[0] == tensor._rank(newshape):
        e = self.flatten
        self.assign(empty=False, form=newform, shape=newshape, data=e, flatten=True)
      else:
        raise shapeform("shape and form doesn't match")
    else:
      raise notshape("shapes don't match")
    
  
  @property
  def transpose(self):
    """returns the transpose of the tensor
        
        Returns
        ------
        tensor
          returns the transpose of the tensor
    """
    fl = self.flatten
    form = tensor.formtranspose(self.form)
    shape = tensor.shapetranspose(self.shape)
    x = tensor.build(form=form, shape=shape, data=fl)
    x.variables = self.variables
    return x
  
  @staticmethod
  def _shape(data):
    """returns the shape of the inputted data
        
        Returns
        ------
        tuple
          returns the shape of the inputted data
    """
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
  
  @staticmethod
  def formdot(form1=(0, 1), form2=(1, 0)):
    """returns the tensor dot product of the inputted forms
        
        Returns
        ------
        tuple
          returns the tensor dot product of the inputted forms
    """
    return (form1[0]+form2[0], form1[1]+form2[1])
  
  @staticmethod
  def shapedot(shape1=(2), shape2=(2)):
    """returns the tensor dot product of the inputted shapes
        
        Returns
        ------
        tuple
          returns the tensor dot product of the inputted shapes
    """
    new = []
    for i in shape1:
      new.append(i)
    for i in shape2:
      new.append(i)
    return tuple(new)
  
  def dot(self, t:tensor, **kwargs):
    """returns the dot product of the self tensor with the t tensor
        
        Returns
        ------
        tensor
          returns the tensor of the dot
    """
    form = tensor.formdot(self.form, t.form)
    shape = tensor.shapedot(self.shape, t.shape)
    data = []
    flattened1 = self.flatten
    flattened2 = t.flatten
    for i in flattened1.data:
      x = []
      for a in flattened2.data:
        x.append(a*i)
      for a in x:
        data.append(a)
    grad = False
    if self.rgrad:
      grad = True
    if t.rgrad:
      grad = True
    return tensor(empty=False, form=form, shape=shape, data=data, flatten=True, rgrad=grad, **kwargs)
  
  @staticmethod
  def build(form=(0, 1), shape=(2), data=[1, 1], **kwargs):
    """returns the built verson of the tensor inputted
        
        Returns
        ------
        tensor
          returns the built verson of the tensor inputted
    """
    new = data
    news = list(shape)
    ls = 1
    for i in news:
      newss = []
      for a in news[:-1]:
        ls *= a
      for a in range(ls):
        x = new[:news[-1]]
        newss.append(x)
        for e in range(len(new[:news[-1]])):
          new.pop(0)
      new = newss
      news.pop()
      ls = 1
    t = tensor(form=form, shape=shape, data=data, flatten=False, **kwargs)
    return t
  
  @property
  def flatten(self):
    """returns the flattened version of the tensor
        
        Returns
        ------
        tensor
          returns the flattened version of the tensor
    """
    flattened = self.data
    s = True
    while s:
        nx = []
        if isinstance(flattened[0], Sequence):
            for i in flattened:
                if isinstance(i, Sequence):
                    for a in i:
                        nx.append(a)
                else:
                    nx.append(i)
            flattened = nx
        else:
            s = False
          
    t = tensor(form=(0, 1), shape=(len(flattened)), data=flattened, flatten=False)
    t.variables = self.variables
    return t
  
  @staticmethod
  def zeros(t=False, form=(1, 1), shape=(2, 2), **kwargs):
    """returns the zero tensor of the inputted form and shape
        
        Returns
        ------
        tensor
          returns the zero tenosr of the inputted form and shape
    """
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
    """returns the 1 tensor of the inputted form and shape
        
        Returns
        ------
        tensor
          returns the 1 tensor of the inputted form and shape
    """
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
    """returns the random(0,1) tensor of the inputted form and shape
        
        Returns
        ------
        tensor
          returns the random(0,1) tensor of the inputted form and shape
    """
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
    """returns the identity matrix of the inputted size
        
        Returns
        ------
        matrix
          returns the identity matrix of the inputted size
    """
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
    """returns the tensor full of the const of the inputted form and shape
        
        Returns
        ------
        tensor
          returns the tensor full of the const of the inputted form and shape
    """
    n = 1
    for i in shape:
      n *= i
    data = []
    for i in range(n):
      data.append(const)
    return tensor(form=form, shape=shape, data=data, flatten=True, **kwargs)
  
  @staticmethod
  def core(form=(0, 1), shape=(2), data=1, **kwargs):
    """returns the tensor with the same numbers for the base of the inputted form and shape
        
        Returns
        ------
        tensor
          returns the tensor with the same numbers for the base of the inputted form and shape
    """
    n = 1
    for i in shape[:-1]:
      n *= i
    other = data
    data = []
    for a in range(n):
      for i in other:
        data.append(i)
    return tensor(form=form, shape=shape, data=data, flatten=True, **kwargs)
    
  def sum(self):
    """returns the sum of the tensor's items
        
        Returns
        ------
        number
          returns the sum of the tensor's items
    """
    s = 0
    x = self.flatten
    for i in x.data:
      s += i
    return s
  
  
  def pretty(self):
    """prints the tensor in a pretty way
    """
    
  def transform(self, jacobian, inversejacobian):
    """transforms tensor
    """
    selfi = ((),())
    return self(, selfi=selfi, )
  
