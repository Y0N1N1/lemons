import math
import os
import random
from collections.abc import Sequence
from lemons.error import Error

"""
Tensor ->
  get_shape
  shape
  assign
  assign_zeros
  assign_identity
"""

class Tensor:
  def __init__(self, data):
    self.data = data
    if not isinstance(data, Sequence):
      self.shape = "error"
      msg = Error("data not list")
      msg.raise_error("TypeError")
    self.shape = Tensor.get_shape(data)
   
#______________________________________________________________________

   def get_shape(lst):
    shape = []
    l = lst
    s = True
    while s:
        shape.append(len(l))
        if isinstance(l[0], Sequence):
            s = True
            l = l[0]
        else:
            s = False
    return shape
  
  
#______________________________________________________________________

  @property
  def shape(self):
    return self.shape
  
#______________________________________________________________________

  @property
  def dtype(self):
    return "tensor"

#______________________________________________________________________

  def assign(self, x):
    self.data = x.data
      
#______________________________________________________________________

  def assign_zeros(self, shape=self.shape, data=[], first=True):
    # shape must be m x n
    self.data = data
    s = math.prod(shape)
    dt = []
    for i in range(s):
      if first:
        self.data.append(0)
      else:
        x = self.data[0:(len(self.data)/s)]
        dt.append(x)
        for i in range(len(self.data)/s):
          self.data.pop(0)
    if not first:
      self.data = dt
    shape.pop()
    self.data = Tensor.assign_zeros(shape=shape, data=self.data, first=false)
    
#_______________________________________________
_______________________

  def assign_identity(self, shape):
    # shape must be n, such that actual shape is n x n
    self.data = []
    for i in range(shape):
      x = [0 for a in range(i)]
      x.append(1)
      for a in range(shape -i -1):
          x.append(0)
      self.data.append(x)
      
#______________________________________________________________________

#end
