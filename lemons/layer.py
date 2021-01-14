import math
import os
import random
from random import random
class Layer:
  class dense:
    def __init__(self, size, activation, bias=None):
      self.size, self.activation = size, activation
      if bias == None:
        self.bias = random()
      else:
        self.bias = bias

    
    def size(self):
      return self.size

    def activation(self):
      return self.activation.__name__
    
    def bias(self):
      return self.bias

    def comp(self, wei):
  