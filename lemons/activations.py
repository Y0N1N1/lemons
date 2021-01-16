import math
import os
import random

"""
Activation ->
  sigmoid
  sigmoid_zero_to_one
  binary_step
  relu
  leaky_relu
  tanh
  elu
  hard_sigmoid
  hard_sigmoid_zero_to_one
  exponential
  identity
  selu
  softplus
  softsign
  swish
  prelu
  softmax
"""
class Activation:
  class sigmoid:
    def comp(value):
      if value > 0:
        res = 1 / (1 + math.exp(-value))
        return res
      else:
        res = -(1 / (1 + math.exp(value)))
        return res

  class sigmoid_zero_to_one:
    def comp(value):
      if value > 0:
        res = 1 / (1 + math.exp(-value))
        return res
      else:
        return 0

  class binary_step:
    def __init__(self, threshold_value):
      self.threshold_value = threshold_value
     
    def comp(self, value):
      if value > self.threshold_value:
        return 1
      if value == self.threshold_value:
        return 1
      else:
        return 0

  class relu:
    def comp(value):
      if value > 0:
        return value
      else: 
        return 0
  
  class leaky_relu:
    def comp(value):
      if value > 0:
        return value
      else: 
        return 0.01 * value
  
  class tanh:
    def comp(value):
      res = (2 / (1 + (math.pow(__functions__.__constants__.euler_constant, (-2 * value))))) -1
      return res

  class elu:
    def comp(value):
      if value > 0:
        return value
      else: 
        return -1
  
  class hard_sigmoid:
    def comp(value):
      if value > 1:
        return 1
      elif value < -1:
        return -1
      else: 
        return value

  class hard_sigmoid_zero_to_one:
    def comp(value):
      if value > 1:
        return 1
      elif value < 0:
        return -1
      else: 
        return value

  class exponential:
    def comp(value):
      return math.exp(value)
  
  class identity:
    def comp(value):
      return value
  
  class selu:
    def comp(value):
      if value > 0:
        return value * 1.05070098 
      else:
        return 1.05070098 * 1.67326324 * ((math.exp(value)) -1)

  class softplus:
    def comp(value):
      return math.log((math.exp(x)) +1)
  
  class softsign:
    def comp(value):
      return x / ((abs(x)) + 1)

  class swish:
    def comp(value):
      if value > 0:
        res = 1 / (1 + math.exp(-value))
        return res * value
      else:
        res = -(1 / (1 + math.exp(value)))
        return res * value
  
  class prelu:
    def __init__(self, multiplier):
      self.multiplier = multiplier
      
    def comp(self, value):
      if value > 0:
        return value
      else: 
        return self.multiplier * value
    
  class softmax:
    def comp(vector):
      res = []
      def total(vec):
        vect = []
        for i in vec:
          x = math.exp(i)
          vect.append(x)
        totalsum = sum(vect)
        return totalsum
      tot = total(vector)
      for i in vector:
        i = math.exp(i) / tot
        res.append(i)
      return res
