import math
import os
import random
from collections.abc import Sequence
from lemons.error import Error

"""
Tensor ->
  raw_get_shape
  shape
  assign
Ideas ->
  zeros
  reshape
Note:
  when a function starts with raw_ it is a "backend function"
  that should only be used by the module yet you can use it if
  you want
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

  def raw_get_shape(self, lst, shape=()):
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

#end
