import math
import os
import random
from random import random 

"""
Layer ->
  dense
"""

class Layer:
  class dense:
    def __init__(self, size, activation, bias=None):
      self.size, self.activation = size, activation
      if bias == None:
        self.bias = random()
      else:
        self.bias = bias

#______________________________________________________________________
    
    def size(self):
      return self.size

#______________________________________________________________________

    def activation(self):
      return self.activation.__name__
    
#______________________________________________________________________

    def bias(self):
      return self.bias

#______________________________________________________________________

    def comp(self, weight_list, neuron_list):
      tot = 0
      for i in range weight_list:
        x = i * neuron_list[i]
        tot += x
      tot += self.bias
      tot = self.activation.comp(tot)
      return tot
  
#______________________________________________________________________

#end
