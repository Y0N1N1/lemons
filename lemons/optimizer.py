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

#______________________________________________________________________

  class sgd:
    # one sample
    def __init__(self, learning_rate):
      self.learning_rate = learning_rate
      self.optimizer = 0
      
    def comp(self, gradient):
      self.optimizer = (old_optimizer - (self.learning_rate * gradient))
      return self.optimizer

#______________________________________________________________________

  class mini_batch_gradient_descent:
    # one batch
    def __init__(self, learning_rate):
      self.learning_rate = learning_rate
      self.optimizer = 0
      
    def comp(self, gradient):
      self.optimizer = (old_optimizer - (self.learning_rate * gradient))
      return self.optimizer

#______________________________________________________________________

  class sgd_momentum:
    def __init__(self, learning_rate, momentum):
      self.learning_rate, self.momentum = learning_rate, momentum
      self.optimizer, self.velocity = 0, 1
      
    def comp(self, gradient):
      self.velocity = (self.momentum * self.velocity) + (self.learning_rate * gradient)
      self.optimizer = (self.optimizer - self.velocity)
      return self.optimizer

#______________________________________________________________________

  class momentum:
    def __init__(self, learning_rate):
      self.learning_rate, self.momentum_decay = learning_rate, momentum_decay
      self.optimizer, self.momentum = 0, 1
      
    def comp(self,  gradient):
      # gradient = objective function(old_optimizer)
      # https://ruder.io/optimizing-gradient-descent/#:~:text=In%20its%20update%20rule%2C%20Adagrad,%CF%B5%20%E2%8B%85%20g%20t%20%2C%20i%20.
      self.momentum = (self.momentum_decay * self.momentum) + (self.learning_rate * gradient)
      self.optimizer = self.optimizer - self.momentum
      return self.optimizer

#______________________________________________________________________

  class nag:
    def __init__(self, learning_rate, momentum_decay):
      self.learning_rate, self.momentum_decay = learning_rate, momentum_decay
      self.optimizer, self.momentum = 0, 1
      
    def comp(self, gradient):
      orr_gradient = self.optimizer - (self.momentum_decay * self.momentum))
      # https://ruder.io/optimizing-gradient-descent/#:~:text=In%20its%20update%20rule%2C%20Adagrad,%CF%B5%20%E2%8B%85%20g%20t%20%2C%20i%20.
      self.momentum = (self.momentum_decay * self.momentum) + (self.learning_rate * orr_gradient)
      self.optimizer = self.optimizer - self.momentum
      return self.optimizer

#______________________________________________________________________

  class sgd_momentum_nesterov:
    def __init__(self, learning_rate, momentum):
      self.learning_rate, self.momentum = learning_rate, momentum
      self.optimizer, self.velocity = 0, 1
      
    def comp(self, gradient):
      self.velocity = (self.momentum * self.velocity) + ((self.learning_rate * gradient)*(self.optimizer - (self.momentum * self.velocity)))
      self.optimizer = (self.optimizer - self.velocity)
      return self.optimizer

#______________________________________________________________________

  class adagrad:
    def __init__(self, learning_rate, fudge_factor):
      self.learning_rate, self.fudge_factor = learning_rate, fudge_factor
      self.opt_list = []
      self.optimizer = 0
   
    def comp(self,  gradient):
        self.opt_list.append(self.optimizer)
        opt_list_val = sum(self.opt_list)
        opt_list_val += ((gradient)*(gradient))
        self.optimizer = (self.optimizer - ((self.learning_rate / (math.sqrt(self.fudge_factor + opt_list_val)))* gradient))
        return self.optimizer
  
#______________________________________________________________________

  class adadelta:
    def __init__(self, fudge_factor, decay_rate):
      self.fudge_factor, self.decay_rate = fudge_factor, decay_rate
      self.update_vector, self.opt_avg, self.update_vector_avg = -1, -1, 1
      self.optimizer = 0
      
    def comp(self, gradient):
      gradient_squared = (gradient)*(gradient)
      self.opt_avg = ( self.decay_rate * self.opt_avg) + (gradient_squared * (1 - self.decay_rate))
      self.update_vector_avg = (self.decay_rate * self.update_vector_avg) + (self.update_vector * (1 - self.decay_rate))
      self.update_vector = -(((math.sqrt(self.update_vector_avg + self.fudge_factor)) / (math.sqrt(self.opt_avg + self.fudge_factor)))*gradient)
      self.optimizer = self.optimizer + self.update_vector
      return  self.optimizer

#______________________________________________________________________

  class rms_prop:
    def __init__(self, learning_rate, fudge_factor, decay_rate):
        self.learning_rate, self.fudge_factor, self.decay_rate = learning_rate, fudge_factor, decay_rate
        self.gradient_avg = 1
        self.optimizer = 0 
      
    def comp(self, gradient):
      gradient_squared = (gradient * gradient)
      self.gradient_avg = (self.decay_rate * self.gradient_avg) + ((1 - self.decay_rate) * gradient_squared)
      self.optimizer = self.optimizer - ((self.learning_rate / math.sqrt(self.gradient_avg + self.fudge_factor)) * gradient)
      return self.optimizer

#______________________________________________________________________

  class adam:
    def __init__(self, learning_rate, fudge_factor,decay_rate_one, decay_rate_two):
      self.decay_rate_one, self.decay_rate_two = decay_rate_one, decay_rate_two
      self.learning_rate, self.fudge_factor = learning_rate, fudge_factor
      self.optimizer = 0
      self.first_moment = 1
      self.second_moment = 1
      
    def comp(self, gradient):
      self.first_moment = (self.decay_rate_one * self.first_moment) + ((1 - self.decay_rate_one) * gradient) # usually: 0.9
      self.second_moment = (self.decay_rate_two * self.second_moment) + ((1 - self.decay_rate_two) * (gradient * gradient)) # usually: 0.999
      self.first_moment = self.first_moment / (1 - self.decay_rate_one)
      self.second_moment = self.second_moment / (1 - self.decay_rate_two)
      self.optimizer = self.optimizer - ((self.learning_rate / (math.sqrt(self.second_moment) + self.fudge_factor)) * self.first_moment)
      return self.optimizer

#______________________________________________________________________

  class adamax:
    def __init__(self, learning_rate, decay_rate_one, decay_rate_two):
      self.decay_rate_one, self.decay_rate_two = decay_rate_one, decay_rate_two
      self.learning_rate = learning_rate
      self.optimizer = 0
      self.first_moment, self.second_moment = 1, 1
      
    def comp(self, gradient):
      self.first_moment = (self.decay_rate_one * self.first_moment) + ((1 - self.decay_rate_one) * gradient) # usually: 0.9
      self.second_moment = max((self.decay_rate_two * self.second_moment) , abs(gradient)) # usually: 0.999
      self.first_moment = self.first_moment / (1 - self.decay_rate_one)
      self.optimizer = self.optimizer - ((self.learning_rate / self.second_moment) * self.first_moment)
      return  self.optimizer

#______________________________________________________________________

  class nadam:
    def __init__(self, learning_rate, fudge_factor, decay_rate_one, decay_rate_two):
      self.learning_rate, self.fudge_factor = learning_rate, fudge_factor
      self.decay_rate_one, self.decay_rate_two = decay_rate_one, decay_rate_two
      self.first_moment, self.second_moment = 1, 1
      self.optimizer = 0
    
    def comp(self, gradient):
      self.first_moment = (self.decay_rate_one * self.first_moment) + ((1 - self.decay_rate_one) * gradient) # usually: 0.9
      self.second_moment = (self.decay_rate_two * self.second_moment) + ((1 - self.decay_rate_two) * (gradient * gradient)) # usually: 0.999
      self.first_moment = self.first_moment / (1 - self.decay_rate_one)
      self.second_moment = self.second_moment / (1 - self.decay_rate_two)
      self.optimizer = self.optimizer - ((self.learning_rate / (math.sqrt(self.second_moment) + self.fudge_factor)) * ((self.decay_rate_one * self.first_moment) + (((1 - self.decay_rate_one) * gradient) / (1 - self.decay_rate_one))))
      return self.optimizer

#______________________________________________________________________

  class amsgrad:
    def __init__(self, learning_rate, fudge_factor, decay_rate_one, decay_rate_two):
      self.learning_rate, self.fudge_factor = learning_rate, fudge_factor
      self.decay_rate_one, self.decay_rate_two = decay_rate_one, decay_rate_two
      self.first_moment, self.second_moment = 1, 1
      self.optimizer = 0
    
    def comp(self, gradient):
      self.first_moment = (self.decay_rate_one * self.first_moment) + ((1 - self.decay_rate_one) * gradient)
      self.second_moment =  (self.decay_rate_two * self.second_moment) + ((1 - self.decay_rate_two) * (gradient * gradient))
      self.second_moment = max(self.bias_second_moment, self.second_moment)
      self.bias_second_moment = self.second_moment
      self.optimizer = self.optimizer - ((self.learning_rate / (sqrt(self.second_moment) + self.fudge_factor)) * self.first_moment)
      return self.optimizer

#______________________________________________________________________
 
#end
