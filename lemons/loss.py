import math
import os
import random

"""
Loss ->
  squared
  absolute
  huber
  epsilon_insensitive
  epsilon_insensitive_squared
  absolute_percentage
  squared_logarithmic
  squared_custom_logarithmic
  locarithmic_cosh
  binary_cross_entropy
  cross_entropy
  custom_log_cross_entropy
  poisson 
  kl_divergence
  hinge
  leaky_hinge
  squared_hinge
  squared_leaky_hinge
  categorical_hinge
  leaky_categorical_hinge
""" 

class Loss:
  class squared:
    def __init__(self):
      self.il = False
      
    def comp(self, y_wanted, y_predicted):
      return (y_predicted - y_wanted) * (y_predicted - y_wanted)
    
    def grad_comp(self, y_wanted, y_predicted):
      return ( 2 * (y_predicted - y_wanted) )
    
#______________________________________________________________________
 
  class absolute:
    def __init__(self):
      self.il = False
      
    def comp(self, y_wanted, y_predicted):
      res = y_predicted - y_wanted
      if res > 0:
        return res
      else: 
        return -res
      
    def grad_comp(self, y_wanted, y_predicted):
      return 1
    
#______________________________________________________________________
 
  class huber:
    def __init__(self, rate):
      self.rate = rate
      self.il = False
    
    def comp(self, y_wanted, y_predicted):
      squared = Loss.squared.comp(y_wanted, y_predicted)
      absolute = Loss.absolute.comp(y_wanted, y_predicted)
      if absolute < self.rate:
        return squared
      else: 
        return absolute
      
    def grad_comp(self, y_wanted, y_predicted):
      squared = Loss.squared.comp(y_wanted, y_predicted)
      absolute = Loss.absolute.comp(y_wanted, y_predicted)
      if absolute < self.rate:
        return Loss.squared.grad_comp(y_wanted, y_predicted)
      else: 
        return Loss.absolute.grad_comp(y_wanted, y_predicted)
      
#______________________________________________________________________
 
  class epsilon_insensitive:
    def __init__(self, rate, bottom):
      self.rate = rate
      self.bottom = bottom
      self.il = False
      
    def comp(self, y_wanted, y_predicted):
      bot = self.bottom
      rat = self.rate
      sub = y_predicted - y_wanted
      if sub >= 0:
        if sub > rat:
          return sub
        else:
          return bot
      else:
        res = abs(sub)
        if res > rat:
          return res
        else:
          return bot
    
    def grad_comp(self, y_wanted, y_predicted):
      bot = self.bottom
      rat = self.rate
      sub = y_predicted - y_wanted
      if sub >= 0:
        if sub > rat:
          return 1
        else:
          return 0
      else:
        res = abs(sub)
        if res > rat:
          return 1
        else:
          return 0
  
#______________________________________________________________________
 
  class epsilon_insentitive_squared:
    def __init__(self, rate, bottom):
      self.rate = rate
      self.bottom = bottom
      self.il = False
      
    def comp(self, y_wanted, y_predicted):
      bot = self.bottom
      rat = self.rate
      sub = y_predicted - y_wanted
      if sub >= 0:
        if sub > rat:
          return (sub * sub)
        else:
          return bot
      else:
        res = abs(sub)
        if res > rat:
          return (res * res)
        else:
          return bot
    
    def grad_comp(self, y_wanted, y_predicted):
      bot = self.bottom
      rat = self.rate
      sub = y_predicted - y_wanted
      if sub >= 0:
        if sub > rat:
          return  (2*(y_predicted - y_wanted))
        else:
          return 0
      else:
        res = abs(sub)
        if res > rat:
          return (2*((y_predicted - y_wanted) / abs(y_predicted - y_wanted) ) ) 
        else:
          return 0
  
#______________________________________________________________________
 
  class absolute_percentage:
    def __init__(self):
      self.il = False
      
    def comp(self, y_wanted, y_predicted):
      return 100 * (abs(y_predicted - y_wanted)/y_wanted)
    
    def grad_comp(self, y_wanted, y_predicted):
      return 100 * ( ((y_predicted - y_wanted) / abs(y_predicted - y_wanted)) /y_wanted)
  
#______________________________________________________________________
 
  class squared_logarithmic:
    def __init__(self):
      self.il = False
      
    def comp(self, y_wanted, y_predicted):
      return ((math.log(y_wanted + 1))*(math.log(y_wanted + 1))-(math.log(y_predicted + 1))
    
    def grad_comp(self, y_wanted, y_predicted):
      return (−(1/(y_predicted+1) ) )
  
#______________________________________________________________________
 
  class squared_custom_logarithmic:
    def __init__(self, custom_base):
      self.custom_base = custom_base
      self.il = False
      
    def comp(self, y_wanted, y_predicted):
      return ((math.log(y_wanted + 1,self.custom_base))*(math.log(y_wanted + 1,self.custom_base)))-(math.log(y_predicted + 1,self.custom_base))
    
    def grad_comp(self, y_wanted, y_predicted):
      return (-(1/(math.log(self.custom_base) *(y_predicted + 1))))
  
#______________________________________________________________________
 
  class logarithmic_cosh:
    def __init__(self):
      self.il = False
              
    def comp(self, y_wanted, y_predicted):
      val = y_predicted - y_wanted
      ex = math.exp(val)
      mex = math.exp(-val)
      return math.log((ex+mex)/2)
    
    def grad_comp(self, y_wanted, y_predicted):
      ex = math.exp(1)
      mex = -math.exp(-1)
      return (1/((ex+mex)/2))

  
#______________________________________________________________________
 
  class binary_cross_entropy:
    def __init__(self):
      self.il = False
   
    def comp(self, y_wanted, y_predicted):
      if y_predicted == 1:
        return -math.log(y_wanted)
      else:
        return -math.log(1 - y_wanted)
    
    def grad_comp(self, y_wanted, y_predicted):
      return 0

#______________________________________________________________________
 
  class cross_entropy:
    def __init__(self, number_of_classes):
      self.number_of_classes = number_of_classes 
      self.il = True
      
    def comp(self, y_meets_wanted_list, y_predicted_list):
      sum_list = [] 
      for i in range(self.number_of_classes):
        wan = y_meets_wanted_list[i]
        pred = y_predicted_list[i]
        if wan == 1:
          res = math.log(pred)
          sum_list.append(res)
        else:
          sum_list.append(0)
      return -sum(sum_list)
    
    def grad_comp(self, y_wanted, y_predicted):
      
  
#______________________________________________________________________
 
  class custom_log_cross_entropy:
    def __init__(self, base, number_of_classes):
      self.base, self.number_of_classes = base, number_of_classes
      self.il = True

    def comp(self, y_meets_wanted_list, y_predicted_list):
      sum_list = []
      for i in range(self.number_of_classes):
        wan = y_meets_wanted_list[i]
        pred = y_predicted_list[i]
        if wan == 1:
          res = math.log(pred,self.base)
          sum_list.append(res)
        else:
          sum_list.append(0)
      return -sum(sum_list)
    
    def grad_comp(self, y_wanted, y_predicted):
      
  
#______________________________________________________________________
  
  class poisson:
    def __init__(self):
      self.il = False
              
    def comp(self, y_wanted, y_predicted):
      return (y_predicted - (y_wanted * math.log(y_predicted)))
    
    def grad_comp(self, y_wanted, y_predicted):
      
  
#______________________________________________________________________
 
  class kl_divergence:
    def __init__(self):
      self.il = False
              
    def comp(self, y_wanted, y_predicted):
      return (y_wanted * math.log(y_wanted / y_predicted))
    
    def grad_comp(self, y_wanted, y_predicted):
      
  
#______________________________________________________________________
 
  class hinge:
    def __init__(self):
      self.il = False
              
    def comp(self, y_wanted, y_predicted):
      #y_wanted MUST be either -1 or 1 (-1: 0, 1: 1). we will auto convert 0 to -1.
      if y_wanted == 0:
        first = 1 - (-1 * y_predicted)
        second = 0
        if first > second:
          return first
        else:
          return second
      else:
        first = 1 - (y_wanted * y_predicted)
        second = 0
        if first > second:
          return first
        else:
          return second
    
    def grad_comp(self, y_wanted, y_predicted):
      
  
#______________________________________________________________________
 
  class leaky_hinge:
    def __init__(self, rate):
      self.rate = rate
      self.il = False
      
    def comp(self, y_wanted, y_predicted):
      #y_wanted MUST be either -1 or 1 (-1: 0, 1: 1). we will auto convert 0 to -1.
      if y_wanted == 0:
        first = 1 - (-1 * y_predicted)
        second = self.rate
        if first > second:
          return first
        else:
          return second
      else:
        first = 1 - (y_wanted * y_predicted)
        second = self.rate
        if first > second:
          return first
        else:
          return second
      
    def grad_comp(self, y_wanted, y_predicted):
      
  
#______________________________________________________________________
 
  class squared_hinge:
    def __init__(self):
      self.il = False
              
    def comp(self, y_wanted, y_predicted):
      #y_wanted MUST be either -1 or 1 (-1: 0, 1: 1). we will auto convert 0 to -1.
      if y_wanted == 0:
        first = (1 - (-1 * y_predicted))*(1 - (-1 * y_predicted))
        second = 0
        if first > second:
          return first
        else:
          return second
      else:
        first = (1 - (y_wanted * y_predicted))*(1 - (y_wanted * y_predicted))
        second = 0
        if first > second:
          return first
        else:
          return second
    
    def grad_comp(self, y_wanted, y_predicted):
      
  
#______________________________________________________________________
 
  class squared_leaky_hinge:
    def __init__(self, rate):
      self.rate = rate
      self.il = False
              
    def comp(self, y_wanted, y_predicted):
      #y_wanted MUST be either -1 or 1 (-1: 0, 1: 1). we will auto convert 0 to -1.
      if y_wanted == 0:
        first = (1 - (-1 * y_predicted))*(1 - (-1 * y_predicted))
        second = self.rate
        if first > second:
          return first
        else:
          return second
      else:
        first = (1 - (y_wanted * y_predicted))*(1 - (y_wanted * y_predicted))
        second = self.rate
        if first > second:
          return first
        else:
          return second
    
    def grad_comp(self, y_wanted, y_predicted):
      
  
#______________________________________________________________________
 
  class categorical_hinge:
    def __init__(self):
      self.il = True
              
    def comp(self, y_wanted_list, y_predicted_list):
      neg = []
      pos = []
      for i in y_wanted_list:
        y_wanted = i
        y_predicted = y_predicted_list[i]
        neg.append((1-y_wanted)*y_predicted)
        pos.append(y_wanted*y_predicted)
      neg_max = max(neg)
      pos_val = sum(pos)
      res = neg_max - pos_val + 1
      return max(res, 0)
    
    def grad_comp(self, y_wanted, y_predicted):
      
  
#______________________________________________________________________
 
  class leaky_categorical_hinge:
    def __init__(self, rate):
      self.rate = rate
      self.il = True
              
    def comp(self, y_wanted_list, y_predicted_list):
      neg = []
      pos = []
      for i in y_wanted_list:
        y_wanted = i
        y_predicted = y_predicted_list[i]
        neg.append((1-y_wanted)*y_predicted)
        pos.append(y_wanted*y_predicted)
      neg_max = max(neg)
      pos_val = sum(pos)
      res = neg_max - pos_val + 1
      return max(res, self.rate)
    
    def grad_comp(self, y_wanted, y_predicted):
      
#______________________________________________________________________
 
#end
