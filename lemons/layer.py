import math
import os
import random
from random import random 

"""
Layer ->
  dense
  average
  maximum
  minimum
  add
  subtract
  multiply
  activation
"""

class Layer:
  class dense:
    def __init__(self, size, activation):
      self.size, self.activation = size, activation
      
#_________________________________
    
    def size(self):
      return self.size

#_________________________________
    
    def activation(self):
      return self.activation.__name__
 
#_________________________________
     
    def comp(self, weight_list, neuron_list, bias):
      tot = 0
      for i, w in enumerate(weight_list):
        x = w * neuron_list[i]
        tot += x
      tot += bias
      tot = self.activation.comp(tot)
      return tot

#_________________________________
    
    def grad_comp(self, weight_list, neuron_list, bias, weight_index):
      return neuron_list[weight_index]

#_________________________________
    
    def bias_grad_comp(self, weight_list, neuron_list, bias):
      return 0
  
#______________________________________________________________________

  class average:
    def __init__(self, size, activation):
      self.size, self.activation = size, activation

#_________________________________
    
    def size(self):
      return self.size

#_________________________________
    
    def activation(self):
      return self.activation.__name__
 
#_________________________________

    def comp(self, weight_list, neuron_list, bias):
      tot = []
      for i, w in enumerate(weight_list):
        x = w * neuron_list[i]
        tot.append(x)
      tot = sum(tot) / len(tot)
      tot += bias
      tot = self.activation.comp(tot)
      return tot
  
#_________________________________
    
    def grad_comp(self, weight_list, neuron_list, bias, weight_index):
      return (neuron_list[weight_index] / len(weight_list))

#_________________________________
    
    def bias_grad_comp(self, weight, neuron, bias):
      return 0
  
#______________________________________________________________________

  class maximum:
    def __init__(self, size, activation):
      self.size, self.activation = size, activation

#_________________________________
    
    def size(self):
      return self.size

#_________________________________
    
    def activation(self):
      return self.activation.__name__
 
#_________________________________
    
    def comp(self, weight_list, neuron_list, bias):
      tot = []
      for i,w in enumerate(weight_list):
        x = w * neuron_list[i]
        tot.append(x)
      tot = max(tot)
      tot += bias
      tot = self.activation.comp(tot)
      return tot
    
#_________________________________
    
    def grad_comp(self, weight_list, neuron_list, bias, weight_index):
      tot = 0
      for i,w in enumerate(weight_list):
        x = w * neuron_list[i]
        if x > tot:
          tot = neuron_list[i]
      return tot

#_________________________________
    
    def bias_grad_comp(self, weight, neuron, bias):
      return 0
  
#______________________________________________________________________

  class minimum:
    def __init__(self, size, activation):
      self.size, self.activation = size, activation

#_________________________________
    
    def size(self):
      return self.size

#_________________________________
    
    def activation(self):
      return self.activation.__name__
 
#_________________________________
    
    def comp(self, weight_list, neuron_list, bias):
      tot = []
      for i,w in enumerate(weight_list):
        x = w * neuron_list[i]
        tot.append(x)
      tot = min(tot)
      tot += bias
      tot = self.activation.comp(tot)
      return tot
      
#_________________________________
    
    def grad_comp(self, weight_list, neuron_list, bias, weight_index):
      tot = 100000
      for i,w in enumerate(weight_list):
        x = w * neuron_list[i]
        if x < tot:
          tot = neuron_list[i]
      return tot

#_________________________________
    
    def bias_grad_comp(self, weight, neuron, bias):
      return 0
  
#______________________________________________________________________

  class add:
    def __init__(self, size, activation):
      self.size, self.activation = size, activation

#_________________________________
    
    def size(self):
      return self.size

#_________________________________
    
    def activation(self):
      return self.activation.__name__
 
#_________________________________
    
    def comp(self, weight_list, neuron_list, bias):
      tot = 0
      for i in neuron_list:
        tot += i
      tot += bias
      tot = self.activation.comp(tot)
      return tot
      
#_________________________________
    
    def grad_comp(self, weight_list, neuron_list, bias, weight_index):
      return 0

#_________________________________
    
    def bias_grad_comp(self, weight, neuron, bias):
      return 0
  
#______________________________________________________________________

  class subtract:
    def __init__(self, size, activation):
      self.size, self.activation = size, activation

#_________________________________
    
    def size(self):
      return self.size

#_________________________________
    
    def activation(self):
      return self.activation.__name__
 
#_________________________________
    
    def comp(self, weight_list, neuron_list, bias):
      tot = 0
      for i in neuron_list:
        tot -= i
      tot += bias
      tot = self.activation.comp(tot)
      return tot
      
#_________________________________
    
    def grad_comp(self, weight_list, neuron_list, bias, weight_index):
      return 0

#_________________________________
    
    def bias_grad_comp(self, weight, neuron, bias):
      return 0
  
#______________________________________________________________________

  class multiply:
    def __init__(self, size, activation):
      self.size, self.activation = size, activation

#_________________________________
    
    def size(self):
      return self.size

#_________________________________
    
    def activation(self):
      return self.activation.__name__
 
#_________________________________
    
    def comp(self, weight_list, neuron_list, bias):
      tot = 1
      for i in neuron_list:
        tot *= i
      tot += bias
      tot = self.activation.comp(tot)
      return tot
      
#_________________________________
    
    def grad_comp(self, weight_list, neuron_list, bias, weight_index):
      return 0

#_________________________________
    
    def bias_grad_comp(self, weight, neuron, bias):
      return 0
  
#______________________________________________________________________

  class activation:
    def __init__(self, size, activation):
      self.size, self.activation = size, activation

#_________________________________
    
    def size(self):
      return self.size

#_________________________________
    
    def activation(self):
      return self.activation.__name__

#_________________________________
    
    def comp(self, weight_list, neuron_list, bias):
      tot = []
      for i in neuron_list:
        x = self.activation.comp(i)
        tot.append(x)
      tot = sum(tot) / len(tot)
      return tot
      
#_________________________________
    
    def grad_comp(self, weight_list, neuron_list, bias, weight_index):
      return 0

#_________________________________
    
    def bias_grad_comp(self, weight, neuron, bias):
      return 0
  
#______________________________________________________________________

#end
