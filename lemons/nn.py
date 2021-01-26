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
    view 
    add 
    back
    foward
    train
    test
    predict
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
      self.bias = []
      for i in self.layer_list:
        self.bias.append(random())
      self.layer_results = []
      self.layer_results_after_activation = []


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
      self.bias.append(random())
    
    def back(self):
      # BACK WEIGHT GRADIENT
      grad_list = []
      for layer in self.network:
        layer_grad_list = []
        for weight in layer:
          weight_grad_list = []
          for data_val in self.layer_results[self.network.index(layer)][layer.index(weight)]:
            data_val_after_activation = self.layer_results_after_activation[self.network.index(layer)][layer.index(weight)][self.layer_results[self.network.index(layer)][layer.index(weight)].index(data_val)]
            weight_val_grad = (self.loss.grad_comp(data_val_after_activation)) * (self.layer_list[self.network.index(layer)].activation.grad_comp(data_val)) * (self.layer_list[self.network.index(layer)].grad_comp(weight))
            weight_grad_list.append(weight_val_grad)
          weight_grad = sum(weight_grad_list) / len(weight_grad_list)
          layer_grad_list.append(weight_grad)
        grad_list.append(layer_grad_list)
      for grad_layer in grad_list:
        for grad in grad_layer:
          optim = self.optimizer.comp(grad)
          self.network[grad_list.index(grad_layer)][grad_layer.index(grad)] -= optim
      # BACK BIAS
      bias_grad_list =  []
      for layer in self.layer_results:
        bias = self.bias[self.layer_results.index(layer)]
        single_bias_grad_list = []
        for point in layer:
          for data_val in point:
            data_val_after_activation = self.layer_results_after_activation[self.layer_results.index(layer)][layer.index(data_val)][point.index(data_val)]
            single_bias_grad = (self.loss.grad_comp(data_val_after_actvation)) * (self.layer_list[self.layer_results.index(layer)].activation.grad_comp(data_val)) * (self.layer_list[self.layer_results.index(layer)].bias_grad_comp(bias))
            single_bias_grad_list.append(single_bias_grad)
        bias_grad = sum(single_bias_grad_list) / len(single_bias_grad_list)
        bias_grad_list.append(bias_grad)
      for bias in self.bias:
        optim = self.optimizer.comp(bias_grad_list[self.bias.index(bias)])
        self.bias[self.bias.index(bias)] -= optim
      
    
    def foward(self, in_data):
      
    
    def train(self, batch_size, epochs, in_data: Tensor, labels: Tensor, show=True):
      # data must be of shape (n, m) and m values must not be lists: e.g.: [[0, 3],[3, 2],[1, 2]] labels: [1, 2, 1], and labels must be of: (n). check data normalization features
      # data and labels must be ordered
      # we expect each data item to be one batch (flatten your data to be (n, m), m = batch size)
      # show will display:
      # epoch loss, metric, progress
      for epoch in range(epochs):
        train_data = in_data.data
        train_labels = labels.data
        for batch in range(batch_size):
            item = train_data[0]
            right = train_labels[0]
            predicted = foward(item)
            loss = self.loss.comp(right, predicted)
            
            train_data.pop(0)
            train_labels.pop(0)
            # SOMEHOW PERFORM BACKPROP

          
      
      
      
      
    def test(self, batch_size, in_data: Tensor, labels: Tensor):
      # data must be of shape (n, m) and m values must not be lists: e.g.: [[0, 3],[3, 2],[1, 2]] labels: [1, 2, 1], and labels must be of: (n). check data normalization features
      # data and labels must be ordered
      # test will return a metric and a loss.
      
    def predict(self, batch_size, in_data: Tensor):
      # data must be of shape (n, m) and m values must not be lists: e.g.: [[0, 3],[3, 2],[1, 2]] 
      # pred will generate a labels matrix shaped (n), and that will be the output
      
      
      
      
      
      
      
      

# substract optimizer from weight (each cost func is with respect to one weight, so that will be the weight to be changed)
