import math
import os
import random
from lemons.layer import Layer
from lemons.loss import Loss
from lemons.optimizer import Optimizer
from lemons.metric import Metric
from lemons.activations import Activation
from lemons.tensor import Tensor
from random import random 
"""
NN ->
  FNN ->
    set_network

Available NNs ->
  FNN
  RNN
  CNN
"""
class NN:
  class FNN:
    def __init__(self, loss: Loss, optimizer: Optimizer, metric: Metric, layer_list = []):
      self.loss, self.optimizer, self.metric = loss, optimizer, metric
      self.layer_list = layer_list
      self.network = []
      first = True
      for _ in self.layer_list:
        weight_count = 1
        if first:
          weight_count = _.size()
          first = False
        else:
          weight_count = _.size() * self.layer_list[self.layer_list.index[_] - 1].size()
        layer = [random() for i in range(weight_count)]
        self.network.append(layer)
        # network will look like:
        #[ [0.1423, 0.8752, 0.5632],
        #  [0.1643,0.8433],
        #  [0.8172, 0.4812]        ]
        # to access a layer: network[layer][weight]
      self.batch_losses = []
      self.gradients = []
      self.epoch_losses = []
      self.testing = []
      self.predicting = []


    def view(self):
      print("Model: FNN")
      print("_________________________________________________________________")
      print("layer______________________activation_____________________size___")
      for i in range(self.layer_count):
        layer = self.layer_list[i].__name__
        activation = self.layer_list[i].activation()
        size = self.layer_size_list[i]
        print(f"{layer}                      {activation}                     {size}   ")
        print("_________________________________________________________________")
      print("_________________________________________________________________")
      print(f"optimizer: {self.optimizer}, loss: {self.loss}, metric: {self.metric}")
      print("_________________________________________________________________")
    
    def add(self, layer: Layer):
      self.layer_list.append(layer)
    
    def back(self):

      derivative_comp - loss, activation, layer - respect to 1 weight, 1 example.
      average weight with all examples:
      #d[Co]/dw -> average out over all training examples: (1/n) * (sum ^n-1 \/ k = 0 of d[Cok]/dw) -> k = specific cost function, n = size
      add to vector of equal dims as network
      #add to gradient vector
      #derivative of cost function with respect to bias -> chain rule -> d[Co]/da * d[a]/dz * d[z]/db 
      # d[Co]/da = derivative of the cost function where a is the respected val,  d[a]/dz = derivative of sigmoid function,  d[z]/db =  derivative of foward function with respect to bias
      #d[Co]/db -> average out over all training examples: (1/n) * (sum ^n-1 \/ k = 0 of d[Cok]/db) -> k = specific cost function, n = size
      #add to bias vector
    
    def foward(self, in_data):
      
    
    def train(self, epochs, in_data: Tensor, labels: Tensor, show=True):
      # data must be of shape (n, m) and m values must not be lists: e.g.: [[0, 3],[3, 2],[1, 2]] labels: [1, 2, 1], and labels must be of: (n). check data normalization features
      # data and labels must be ordered
      # we expect each data item to be one batch (flatten your data to be (n, m), m = batch size)
      # show will display:
      # epoch loss, metric, progress
      for epoch in range(epochs):
        for batch in range(in_data.data):
          right = labels.data[batch]
          predicted = foward(batch)
          loss = self.loss.comp(right, predicted)
          # SOMEHOW PERFORM BACKPROP
          
          
      
      
      
      
    def test(batch_size, in_data: Tensor, labels: Tensor):
      # data must be of shape (n, m) and m values must not be lists: e.g.: [[0, 3],[3, 2],[1, 2]] labels: [1, 2, 1], and labels must be of: (n). check data normalization features
      # data and labels must be ordered
      # test will return a metric and a loss.
      
    def pred(batch_size, in_data: Tensor):
      # data must be of shape (n, m) and m values must not be lists: e.g.: [[0, 3],[3, 2],[1, 2]] 
      # pred will generate a labels matrix shaped (n), and that will be the output
      
      
      
      
      
      
      
      

# substract optimizer from weight (each cost func is with respect to one weight, so that will be the weight to be changed)
