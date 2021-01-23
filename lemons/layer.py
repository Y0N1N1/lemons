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
    def __init__(self, size, activation, bias=None):
      self.size, self.activation = size, activation
      if bias == None:
        self.bias = -random.randint(0,10)
      else:
        self.bias = bias

#_________________________________
    
    def size(self):
      return self.size

#_________________________________
    
    def activation(self):
      return self.activation.__name__
 
#_________________________________
    
    def bias(self):
      return self.bias

#_________________________________
     
    def comp(self, weight_list, neuron_list):
      tot = 0
      for i in range(weight_list):
        x = i * neuron_list[i]
        tot += x
      tot += self.bias
      tot = self.activation.comp(tot)
      return tot
  
#______________________________________________________________________

  class average:
    def __init__(self, size, activation, bias=None):
      self.size, self.activation = size, activation
      if bias == None:
        self.bias = -random.randint(0,10)
      else:
        self.bias = bias

#_________________________________
    
    def size(self):
      return self.size

#_________________________________
    
    def activation(self):
      return self.activation.__name__
 
#_________________________________
    
    def bias(self):
      return self.bias

#_________________________________
    
    def comp(self, weight_list, neuron_list):
      tot = []
      for i in range(weight_list):
        x = i * neuron_list[i]
        tot.append(x)
      tot = sum(tot) / len(tot)
      tot += self.bias
      tot = self.activation.comp(tot)
      return tot
  
#______________________________________________________________________

  class maximum:
    def __init__(self, size, activation, bias=None):
      self.size, self.activation = size, activation
      if bias == None:
        self.bias = -random.randint(0,10)
      else:
        self.bias = bias

#_________________________________
    
    def size(self):
      return self.size

#_________________________________
    
    def activation(self):
      return self.activation.__name__
 
#_________________________________
    
    def bias(self):
      return self.bias

#_________________________________
    
    def comp(self, weight_list, neuron_list):
      tot = []
      for i in range(weight_list):
        x = i * neuron_list[i]
        tot.append(x)
      tot = max(tot)
      tot += self.bias
      tot = self.activation.comp(tot)
      return tot
  
#______________________________________________________________________

  class minimum:
    def __init__(self, size, activation, bias=None):
      self.size, self.activation = size, activation
      if bias == None:
        self.bias = -random.randint(0,10)
      else:
        self.bias = bias

#_________________________________
    
    def size(self):
      return self.size

#_________________________________
    
    def activation(self):
      return self.activation.__name__
 
#_________________________________
    
    def bias(self):
      return self.bias

#_________________________________
    
    def comp(self, weight_list, neuron_list):
      tot = []
      for i in range(weight_list):
        x = i * neuron_list[i]
        tot.append(x)
      tot = min(tot)
      tot += self.bias
      tot = self.activation.comp(tot)
      return tot
  
#______________________________________________________________________

  class add:
    def __init__(self, size, activation, bias=None):
      self.size, self.activation = size, activation
      if bias == None:
        self.bias = -random.randint(0,10)
      else:
        self.bias = bias

#_________________________________
    
    def size(self):
      return self.size

#_________________________________
    
    def activation(self):
      return self.activation.__name__
 
#_________________________________
    
    def bias(self):
      return self.bias

#_________________________________
    
    def comp(self, weight_list, neuron_list):
      tot = 0
      for i in range(neuron_list):
        tot += i
      tot += self.bias
      tot = self.activation.comp(tot)
      return tot
  
#______________________________________________________________________

  class subtract:
    def __init__(self, size, activation, bias=None):
      self.size, self.activation = size, activation
      if bias == None:
        self.bias = -random.randint(0,10)
      else:
        self.bias = bias

#_________________________________
    
    def size(self):
      return self.size

#_________________________________
    
    def activation(self):
      return self.activation.__name__
 
#_________________________________
    
    def bias(self):
      return self.bias

#_________________________________
    
    def comp(self, weight_list, neuron_list):
      tot = 0
      for i in range(neuron_list):
        tot -= i
      tot += self.bias
      tot = self.activation.comp(tot)
      return tot
  
#______________________________________________________________________

  class multiply:
    def __init__(self, size, activation, bias=None):
      self.size, self.activation = size, activation
      if bias == None:
        self.bias = -random.randint(0,10)
      else:
        self.bias = bias

#_________________________________
    
    def size(self):
      return self.size

#_________________________________
    
    def activation(self):
      return self.activation.__name__
 
#_________________________________
    
    def bias(self):
      return self.bias

#_________________________________
    
    def comp(self, weight_list, neuron_list):
      tot = 1
      for i in range(neuron_list):
        tot *= i
      tot += self.bias
      tot = self.activation.comp(tot)
      return tot
  
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
    
    def comp(self, weight_list, neuron_list):
      tot = []
      for i in range(neuron_list):
        x = self.activation.comp(i)
        tot.append(x)
      tot = sum(tot) / len(tot)
      return tot
  
#______________________________________________________________________

#end
