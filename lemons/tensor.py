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
Ideas ->
  zeros
  reshape

"""

class Tensor:
  def __init__(self, data):
    self.data = data
    if not isinstance(data, Sequence):
      self.shape = "error"
      msg = Error("data not list")
      msg.raise_error("TypeError")
    self.shape = raw_get_shape(data)
   
#______________________________________________________________________

  def get_shape(self, lst, shape=()):
    if not isinstance(lst, Sequence):
        # base case
        return shape
    if isinstance(lst[0], Sequence):
        l = len(lst[0])
        if not all(len(item) == l for item in lst):
            msg = Error('not all lists have the same length')
            msg.raise_error("ValueError")
    shape += (len(lst), )
    # recurse
    shape = get_shape(lst[0], shape)
    return shape
  
#______________________________________________________________________

  @property
  def shape(self):
    return self.shape
  
#______________________________________________________________________

  def assign(self, x):
    self.data = x.data
      
#______________________________________________________________________

  def assign_zeros(self, shape):
    # shape must be m x n
    self.data = []
    for i in range(shape[0]):
      x = [0 for a in range(shape[1])]
      self.data.append(x)
  
  def assign_identity(self, shape):
    # shape must be m x n
    self.data = []
    for i in range(shape[0]):
      x = [0 for a in range(i)]
      x.append(1)
      x.append(0) for a in range(shape[0] -i)
      self.data.append(x)
      
    

#end
