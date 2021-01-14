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
  def sigmoid(value):
    if value > 0:
      res = 1 / (1 + math.exp(-value))
      return res
    else:
      res = -(1 / (1 + math.exp(value)))
      return res

  def sigmoid_zero_to_one(value):
    if value > 0:
      res = 1 / (1 + math.exp(-value))
      return res
    else:
      return 0

  def binary_step(value, threshold_value):
    if value > threshold_value:
      return 1
    if value == threshold_value:
      return 1
    else:
      return 0

  def relu(value):
    if value > 0:
      return value
    else: 
      return 0

  def leaky_relu(value):
    if value > 0:
      return value
    else: 
      return 0.01 * value

  def tanh(value):
    res = (2 / (1 + (math.pow(__functions__.__constants__.euler_constant, (-2 * value))))) -1
    return res

  def elu(value):
    if value > 0:
      return value
    else: 
      return -1
  
  def hard_sigmoid(value):
    if value > 1:
      return 1
    elif value < -1:
      return -1
    else: 
      return value

  def hard_sigmoid_zero_to_one(value):
    if value > 1:
      return 1
    elif value < 0:
      return -1
    else: 
      return value

  def exponential(value):
    return math.exp(value)
  
  def indentity(value):
    return value

  def selu(value):
    if value > 0:
      return value * 1.05070098 
    else:
      return 1.05070098 * 1.67326324 * ((math.exp(value)) -1)

  def softplus(value):
    return math.log((math.exp(x)) +1)

  def softsign(value):
    return x / ((abs(x)) + 1)

  def swish(value):
    if value > 0:
      res = 1 / (1 + math.exp(-value))
      return res * value
    else:
      res = -(1 / (1 + math.exp(value)))
      return res * value
  
  def prelu(value, multiplier):
    if value > 0:
      return value
    else: 
      return multiplier * value

  def softmax(vector):
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