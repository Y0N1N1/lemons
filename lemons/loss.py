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
  def squared(y_wanted, y_predicted):
    return (y_wanted - y_predicted) * (y_wanted - y_predicted)

  
#______________________________________________________________________
 
  def absolute(y_wanted, y_predicted):
    res = y_wanted - y_predicted
    if res > 0:
      return res
    else: 
      return -res

  
#______________________________________________________________________
 
  def huber(rate, y_wanted, y_predicted):
    r = rate
    squared = __functions__.__loss_function__.squared(y_wanted, y_predicted)
    absolute = __functions__.__loss_function__.absolute(y_wanted, y_predicted)
    if absolute < rate:
      return squared
    else: 
      return absolute

  
#______________________________________________________________________
 
  def epsilon_insensitive(rate, bottom, y_wanted, y_predicted):
    bot = bottom
    rat = rate
    sub = y_wanted - y_predicted
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

  
#______________________________________________________________________
 
  def epsilon_insensitive_squared(rate, bottom, y_wanted, y_predicted):
    bot = bottom
    rat = rate
    sub = y_wanted - y_predicted
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

  
#______________________________________________________________________
 
  def absolute_percentage(y_wanted, y_predicted):
    return 100 * (abs(y_wanted - y_predicted)/y_wanted)

  
#______________________________________________________________________
 
  def squared_logarithmic(y_wanted, y_predicted):
    return ((math.log(y_wanted + 1))*(math.log(y_wanted + 1)))-(math.log(y_predicted + 1))
  
  
#______________________________________________________________________
 
  def squared_custom_logarithmic(custom_base, y_wanted, y_predicted):
    return ((math.log(y_wanted + 1,custom_base))*(math.log(y_wanted + 1,custom_base)))-(math.log(y_predicted + 1,custom_base))

  
#______________________________________________________________________
 
  def logarithmic_cosh(y_predicted, y_wanted):
    val = y_predicted - y_wanted
    ex = math.exp(val)
    mex = math.exp(-val)
    return math.log((ex+mex)/2)

  
#______________________________________________________________________
 
  def binary_cross_entropy(y_wanted, y_predicted):
    if y_predicted == 1:
      return -math.log(y_wanted)
    else:
      return -math.log(1 - y_wanted)

  
#______________________________________________________________________
 
  def cross_entropy(number_of_classes, y_meets_wanted_list, y_predicted_list):
    sum_list = []
    for i in range(number_of_classes):
      wan = y_meets_wanted_list[i]
      pred = y_predicted_list[i]
      if wan == 1:
        res = math.log(pred)
        sum_list.append(res)
      else:
        sum_list.append(0)
    return -sum(sum_list)

  
#______________________________________________________________________
 
  def custom_log_cross_entropy(base, number_of_classes, y_meets_wanted_list, y_predicted_list):
    sum_list = []
    for i in range(number_of_classes):
      wan = y_meets_wanted_list[i]
      pred = y_predicted_list[i]
      if wan == 1:
        res = math.log(pred,base)
        sum_list.append(res)
      else:
        sum_list.append(0)
    return -sum(sum_list)

  
#______________________________________________________________________
 
  def poisson(y_wanted, y_predicted):
    return (y_predicted - (y_wanted * math.log(y_predicted)))

  
#______________________________________________________________________
 
  def kl_divergence(y_wanted, y_predicted):
    return (y_wanted * math.log(y_wanted / y_predicted))

  
#______________________________________________________________________
 
  def hinge(y_wanted, y_predicted):
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

  
#______________________________________________________________________
 
  def leaky_hinge(rate, y_wanted, y_predicted):
    #y_wanted MUST be either -1 or 1 (-1: 0, 1: 1). we will auto convert 0 to -1.
    if y_wanted == 0:
      first = 1 - (-1 * y_predicted)
      second = rate
      if first > second:
        return first
      else:
        return second
    else:
      first = 1 - (y_wanted * y_predicted)
      second = rate
      if first > second:
        return first
      else:
        return second
  
  
#______________________________________________________________________
 
  def squared_hinge(y_wanted, y_predicted):
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

  
#______________________________________________________________________
 
  def squared_leaky_hinge(rate, y_wanted, y_predicted):
    #y_wanted MUST be either -1 or 1 (-1: 0, 1: 1). we will auto convert 0 to -1.
    if y_wanted == 0:
      first = (1 - (-1 * y_predicted))*(1 - (-1 * y_predicted))
      second = rate
      if first > second:
        return first
      else:
        return second
    else:
      first = (1 - (y_wanted * y_predicted))*(1 - (y_wanted * y_predicted))
      second = rate
      if first > second:
        return first
      else:
        return second

  
#______________________________________________________________________
 
  def categorical_hinge(y_wanted_list, y_predicted_list):
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
  
  
#______________________________________________________________________
 
  def leaky_categorical_hinge(rate, y_wanted_list, y_predicted_list):
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
    return max(res, rate)
  
#______________________________________________________________________
 
#end
