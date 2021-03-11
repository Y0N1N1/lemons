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
  #softmax
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

#______________________________________________________________________

    def grad_comp(value):
      return (Activation.sigmoid.comp(value) * (1 - Acivation.sigmoid.comp(value)))
#______________________________________________________________________

  class sigmoid_zero_to_one:
    def comp(value):
      if value > 0:
        res = 1 / (1 + math.exp(-value))
        return res
      else:
        return 0

#______________________________________________________________________

    def grad_comp(value):
      res = Activation.sigmoid.grad_comp(value)
      if value > 0:
       return res
      else:
       return 0
#______________________________________________________________________

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

#______________________________________________________________________

    def grad_comp(value):
      return 0
#______________________________________________________________________

  class relu:
    def comp(value):
      if value > 0:
        return value
      else: 
        return 0
  
#______________________________________________________________________

    def grad_comp(value):
      if value > 0:
        return 1
      else:
        return 0
#______________________________________________________________________

  class leaky_relu:
    def comp(value):
      if value > 0:
        return value
      else: 
        return 0.01 * value
  
#______________________________________________________________________

    def grad_comp(value):
      if value > 0:
        return 1
      else:
        return 0.01
#______________________________________________________________________

  class tanh:
    def comp(value):
      res = (2 / (1 + (math.pow(2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274, (-2 * value))))) -1
      return res

#______________________________________________________________________

    def grad_comp(value):
      return (1 - (Activation.tanh.comp(value) * Activation.tanh.comp(value)))
#______________________________________________________________________

  class elu:
    def comp(value):
      if value > 0:
        return value
      else: 
        return -1
  
#______________________________________________________________________

    def grad_comp(value):
      if value > 0:
        return 1
      else:
        return 0

#______________________________________________________________________

  class hard_sigmoid:
    def comp(value):
      if value > 1:
        return 1
      elif value < -1:
        return -1
      else: 
        return value

#______________________________________________________________________

    def grad_comp(value):
      if value > 1:
        return 0
      elif value < -1:
        return 0
      else:
        return 1
#______________________________________________________________________

  class hard_sigmoid_zero_to_one:
    def comp(value):
      if value > 1:
        return 1
      elif value < 0:
        return -1
      else: 
        return value

#______________________________________________________________________

    def grad_comp(value):
      if value > 1:
        return 0
      elif value < 0:
        return 0
      else:
       return 1

#______________________________________________________________________

  class exponential:
    def comp(value):
      return math.exp(value)
  
#______________________________________________________________________

    def grad_comp(value):
      return math.exp(value)

#______________________________________________________________________

  class identity:
    def comp(value):
      return value
  
#______________________________________________________________________

    def grad_comp(value):
      return 1
#______________________________________________________________________

  class selu:
    def comp(value):
      if value > 0:
        return value * 1.05070098 
      else:
        return 1.05070098 * 1.67326324 * ((math.exp(value)) -1)

#______________________________________________________________________

    def grad_comp(value):
      if value > 0:
        return 1.05070098 
      else:
        return 1.05070098 * 1.67326324 * (math.exp(value))

#______________________________________________________________________

  class softplus:
    def comp(value):
      return math.log((math.exp(value)) +1)
  
#______________________________________________________________________

    def grad_comp(value):
      return 1 / (1 + math.exp(−value))

#______________________________________________________________________

  class softsign:
    def comp(value):
      return (value / ((abs(value)) + 1))

#______________________________________________________________________

    def grad_comp(value):
      return (1 / ( (1 + abs(value)) *(1 + abs(value)) )
#______________________________________________________________________

  class swish:
    def comp(value):
      if value > 0:
        res = 1 / (1 + math.exp(-value))
        return res * value
      else:
        res = -(1 / (1 + math.exp(value)))
        return res * value
  
#______________________________________________________________________

    def grad_comp(value):
      return (Activation.swish.comp(value) + (Activation.sigmoid.comp(value) * (1 - Activation.swish.comp(value))))
              
#______________________________________________________________________

  class prelu:
    def __init__(self, multiplier):
      self.multiplier = multiplier
      
    def comp(self, value):
      if value > 0:
        return value
      else: 
        return self.multiplier * value
    
#______________________________________________________________________

    def grad_comp(value):
      if value > 0:
        return 1
      else:
        return self.multiplier

#______________________________________________________________________

  #class softmax:
  #  def comp(vector):
  #    res = []
  #    def total(vec):
  #      vect = []
  #      for i in vec:
  #        x = math.exp(i)
  #        vect.append(x)
  #      totalsum = sum(vect)
  #      return totalsum
  #    tot = total(vector)
  #    for i in vector:
  #      i = math.exp(i) / tot
  #      res.append(i)
  #    return res

#______________________________________________________________________
 
#end
