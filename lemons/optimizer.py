import math
import os
import random

"""
Optimizer ->
  gradient_descent
  sgd
  mini_batch_gradient_descent
  sgd_momentum
  momentum
  nag
  sgd_momentum_nesterov
  adagrad
  adadelta
  rms_prop
  adam
  adamax
  nadam
  amsgrad

future ideas ->
  lbfgs
  ftrl
  Conjugate Gradients
  BFGS
  Newton’s Method
  adamw
"""

class Optimizer:
  class gradient_descent:
    # whole training epoch
    def __init__(self, learning_rate):
      self.learning_rate = learning_rate
      self.optimizer = 0
      
    def comp(self, gradient):
      self.optimizer = (old_optimizer - (self.learning_rate * gradient))
      return self.optimizer
  
  class sgd:
    # one sample
    def __init__(self, learning_rate):
      self.learning_rate = learning_rate
      self.optimizer = 0
      
    def comp(self, gradient):
      self.optimizer = (old_optimizer - (self.learning_rate * gradient))
      return self.optimizer
  
  class mini_batch_gradient_descent:
    # one batch
    def __init__(self, learning_rate):
      self.learning_rate = learning_rate
      self.optimizer = 0
      
    def comp(self, gradient):
      self.optimizer = (old_optimizer - (self.learning_rate * gradient))
      return self.optimizer

  def sgd_momentum(old_optimizer, old_velocity, momentum, learning_rate, gradient):
    velocity = (momentum * old_velocity) + (learning_rate * gradient)
    optimizer = (old_optimizer - velocity)
    return velocity, optimizer
  
  def momentum(old_optimizer, old_momentum, momentum_decay, learning_rate, gradient):
    # gradient = objective function(old_optimizer)
    # https://ruder.io/optimizing-gradient-descent/#:~:text=In%20its%20update%20rule%2C%20Adagrad,%CF%B5%20%E2%8B%85%20g%20t%20%2C%20i%20.
    momentum = (momentum_decay * old_momentum) + (learning_rate * gradient)
    optimizer = old_optimizer - momentum
    return momentum, optimizer
  
  def nag(old_optimizer, old_momentum, momentum_decay, learning_rate, gradient):
    # gradient = objective function(old_optimizer - (momentum_decay * old_momentum))
    # https://ruder.io/optimizing-gradient-descent/#:~:text=In%20its%20update%20rule%2C%20Adagrad,%CF%B5%20%E2%8B%85%20g%20t%20%2C%20i%20.
    momentum = (momentum_decay * old_momentum) + (learning_rate * gradient)
    optimizer = old_optimizer - momentum
    return momentum, optimizer

  def sgd_momentum_nesterov(old_optimizer, old_velocity, momentum, learning_rate, gradient):
    velocity = (momentum * old_velocity) + ((learning_rate * gradient)*(old_optimizer - (momentum * old_velocity)))
    optimizer = (old_optimizer - velocity)
    return velocity, optimizer
  
  def adagrad(old_optimizer, learning_rate, fudge_factor, gradient, old_opt_list):
    opt_list = old_opt_list
    opt_list_val = sum(opt_list)
    opt_list_val += ((gradient)*(gradient))
    optimizer = (old_optimizer - ((learning_rate / (math.sqrt(fudge_factor + opt_list_val)))* gradient))
    return opt_list_val, optimizer
  
  def adadelta(old_optimizer, fudge_factor, gradient, old_opt_avg, decay_rate, old_update_vector, old_update_vector_avg):
    gradient_squared = (gradient)*(gradient)
    opt_avg = ( decay_rate * old_opt_avg) + (gradient_squared * (1 - decay_rate))
    update_vector_avg = (decay_rate * old_update_vector_avg) + (old_update_vector * (1 - decay_rate))
    update_vector = -(((math.sqrt(update_vector_avg + fudge_factor)) / (math.sqrt(opt_avg + fudge_factor)))*gradient)
    optimizer = old_optimizer + update_vector
    return update_vector_avg, update_vector, opt_avg, optimizer

  def rms_prop(gradient, old_gradient_avg, decay_rate, old_optimizer, learning_rate, fudge_factor):
    gradient_squared = (gradient * gradient)
    gradient_avg = (decay_rate * old_gradient_avg) + ((1 - decay_rate) * gradient_squared)
    optimizer = old_optimizer - ((learning_rate / math.sqrt(gradient_avg + fudge_factor)) * gradient)
    return gradient_avg, optimizer

  def adam(gradient, decay_rate_one, decay_rate_two, learning_rate, fudge_factor, old_first_moment, old_second_moment, old_optimizer):
    first_moment = (decay_rate_one * old_first_moment) + ((1 - decay_rate_one) * gradient) # usually: 0.9
    second_moment = (decay_rate_two * old_second_moment) + ((1 - decay_rate_two) * (gradient * gradient)) # usually: 0.999
    bias_corrected_first_moment = first_moment / (1 - decay_rate_one)
    bias_corrected_second_moment = second_moment / (1 - decay_rate_two)
    optimizer = old_optimizer - ((learning_rate / (math.sqrt(bias_corrected_second_moment) + fudge_factor)) * bias_corrected_first_moment)
    return bias_corrected_first_moment, bias_corrected_second_moment, optimizer

  def adamax(gradient, decay_rate_one, decay_rate_two, learning_rate, old_first_moment, old_second_moment, old_optimizer):
    first_moment = (decay_rate_one * old_first_moment) + ((1 - decay_rate_one) * gradient) # usually: 0.9
    second_moment = max((decay_rate_two * old_second_moment) , abs(gradient)) # usually: 0.999
    bias_corrected_first_moment = first_moment / (1 - decay_rate_one)
    optimizer = old_optimizer - ((learning_rate / second_moment) * bias_corrected_first_moment)
    return bias_corrected_first_moment, second_moment, optimizer

  def nadam(gradient, decay_rate_one, decay_rate_two, learning_rate, fudge_factor, old_first_moment, old_second_moment, old_optimizer):
    first_moment = (decay_rate_one * old_first_moment) + ((1 - decay_rate_one) * gradient) # usually: 0.9
    second_moment = (decay_rate_two * old_second_moment) + ((1 - decay_rate_two) * (gradient * gradient)) # usually: 0.999
    bias_corrected_first_moment = first_moment / (1 - decay_rate_one)
    bias_corrected_second_moment = second_moment / (1 - decay_rate_two)
    optimizer = old_optimizer - ((learning_rate / (math.sqrt(bias_corrected_second_moment) + fudge_factor)) * ((decay_rate_one * bias_corrected_first_moment) + (((1 - decay_rate_one) * gradient) / (1 - decay_rate_one))))
    return bias_corrected_first_moment, bias_corrected_second_moment, optimizer

  def amsgrad(gradient, decay_rate_one, decay_rate_two, old_first_moment, old_second_moment, old_bias_corrected_second_moment, old_optimizer, learning_rate, fudge_factor):
    first_moment = (decay_rate_one * old_first_moment) + ((1 - decay_rate_one) * gradient)
    second_moment =  (decay_rate_two * old_second_moment) + ((1 - decay_rate_two) * (gradient * gradient))
    bias_corrected_second_moment = max(old_bias_corrected_second_moment, second_moment)
    optimizer = old_optimizer - ((learning_rate / (sqrt(bias_corrected_second_moment) + fudge_factor)) * first_moment)
    return first_moment, second_moment, bias_corrected_second_moment, optimizer
