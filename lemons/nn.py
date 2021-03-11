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
    save
"""
class NN:
  class FNN:
    def __init__(self, input_length, loss: Loss, optimizer: Optimizer, metric: Metric, layer_list = []):
      # tools
      self.loss, self.optimizer, self.metric = loss, optimizer, metric
      # layers
      self.layer_list = layer_list
      # weight tensor
      self.weight_tensor = []
      # make weight tensor
      length = len(self.layer_list)
      first = True
      for i in range(length):
        ll = 0
        if first:
          ll = input_length
          first = False
        else:
          ll = self.layer_list[i-1].size()
        l = self.layer_list[i+1].layer_weight_tensor(ll)
        self.weight_tensor.append(l)
      # bias tensor
      self.bias_tensor = []
      # make bias tensor
      for layer in self.layer_list:
        self.bias_tensor.append(random())
      # stuff for backprop
      self.layer_results = []
      self.layer_results_after_activation = []
      # make ^^^
      for i in range(length - 1):
        ll = self.layer_list[i].size()
        lll = self.layer_list[i+1].size()
        l = []
        for i in range(lll):
          x = []
          for i in range(ll):
            x.append([])
          l.append(x)
        self.layer_results.append(l)
        self.layer_results_after_activation.append(l)
      # done


    def view(self):
      print("Model: FNN")
      print("_________________________________________________________________")
      print("layer______________________activation_____________________size___")
      for i in range(len(self.layer_list)):
        layer = self.layer_list[i].__name__
        activation = self.layer_list[i].activation()
        size = self.layer_size_list[i]
        print(f"{layer}                      {activation}                     {size}   ")
        print("_________________________________________________________________")
      print("_________________________________________________________________")
      print(f"optimizer: {self.optimizer.__name__}, loss: {self.loss.__name__}, metric: {self.metric.__name__}")
      print("_________________________________________________________________")
    
    
    def back(self):
      # Back weight
      #     create grad tensor
      grad_tensor = []
      for layer in self.weight_tensor:
        l = []
        for neuron in layer:
          x = []
          for last_neuron in neuron:
            y = []
            x.append(y)
          l.append(x)
        grad_tensor.append(l)
      #     calculate grad
      for lindx, layer in enumerate(self.weight_tensor):
        for nindx, neuron in enumerate(layer):
          for lnindx, last_neuron in enumerate(neuron):
          # bias grad samples
          grad_samples = []
          for sindx, sample in enumerate(self.layer_results[lindx][nindx][lnindx]):
            if len(last_neuron) == 0:
              pass
            else:
              weight = last_neuron[0]
              result = sample
              result_after_activation = self.layer_results_after_activation[lindx][nindx][lnindx][sindx]
              single_grad = (self.loss.grad_comp(result_after_activation)) * (self.layer_list[lindx].activation.grad_comp(result)) * (self.layer_list[lindx].grad_comp(weight))
              grad_samples.append(single_grad)
          grad = sum(grad_samples) / len(grad_samples)
          grad_tensor[lindx][nindx][lnindx].append(grad)
      #     apply optimizer
      for lindx, layer in enumerate(self.weight_tensor):
        for nindx, neuron in enumerate(layer):
          for lnindx, last_neuron in enumerate(neuron):
            if len(last_neuron) == 0:
              pass
            else:
              self.weight_tensor[lindx][nindx][lnindx][0] = self.weight_tensor[lindx][nindx][lnindx][0] - self.optimizer.comp(grad_tensor[lindx][nindx][lnindx][0])
      # Back bias
      #     create bias grad tensor
      bias_grad_tensor = []
      #     calculate grad
      for lindx, bias in enumerate(self.bias_tensor):
        # bias grad samples
        bias_grad_samples = []
        for nindx, neuron in enumerate(self.layer_results[bindx]):
          for lnindx, last_neuron in enumerate(neuron):
            for sindx, sample in enumerate(last_neuron):
              bias = self.bias_tensor[lindx]
              result = sample
              result_after_activation = self.layer_results_after_activation[lindx][nindx][lnindx][sindx]
              single_grad = (self.loss.grad_comp(result_after_activation)) * (self.layer_list[lindx].activation.grad_comp(result)) * (self.layer_list[lindx].bias_grad_comp(bias))
              bias_grad_samples.append(single_grad)
        grad = sum(bias_grad_samples) / len(bias_grad_samples)
        bias_grad_tensor.append(grad)
      #     apply optimizer
      for indx, grad in enumerate(bias_grad_tensor):
        self.bias_tensor[indx] = self.bias_tensor[indx] -self.optimizer.comp(grad)
      
      
    
    def foward(self, data_vector):
      # vector being fowarded through the network
      neuron_vals = data_vector
      # iterating through each layer
      for lindx, layer in enumerate(self.layer_list):
        # new vector
        new_neuron_vals = []
        # iterating through each neuron
        for indx, neuron in enumerate(neuron_vals):
          previous_neuron_index = []
          # create a weight vector
          weight_vector = []
          for last_neuron_index, last_neuron in enumerate(self.weight_tensor[lindx][indx]):
            if len(last_neuron) == 0:
              pass
            else:
              previous_neuron_index.append(last_neuron_index)
              weight_vector.append(last_neuron[0])
          # create neuron vector
          neuron_vector = []
          for last_neuron_index in previous_neuron_index:
            neuron_vector.append(neuron_vals[last_neuron_index])
          # get bias
          bias = self.bias_tensor[lindx]
          # calculate new value
          result, result_before_activation = layer.comp(weight_vector, neuron_vector, bias)
          # append result to new_neuron_vals
          new_neuron_vals.append(result)
          # layer_results_after_activation append values
          for last_neuron_index, last_neuron in enumerate(self.layer_results_after_activation[lindx][indx]):
            for chosen_indexes in previous_neuron_index:
              if chosen_indexes == last_neuron_index:
                self.layer_results_after_activation[lindx][indx][last_neuron_index].append(result)
          # layer_results append values
          for last_neuron_index, last_neuron in enumerate(self.layer_results[lindx][indx]):
            for chosen_indexes in previous_neuron_index:
              if chosen_indexes == last_neuron_index:
                self.layer_results[lindx][indx][last_neuron_index].append(result_before_activation)
        # updating vector
        neuron_vals = new_neuron_vals
      return neuron_vals
      # stores  layer_results_after_activation, layer_results
      # returns label_vector
        
      
      
    
    def train(self, batch_size, epochs, data_matrix : Tensor, label_vector : Tensor, show=True):
      # data must be of shape (n, m), a matrix
      # label vector must be of shape (n), a vector
      # data and labels must be in order
      # show will display:
      # epoch loss, metric, progress
      # train will output a final loss and metric
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
            
            ##### loss il
            ##### tqdm
 
    def test(self, batch_size, data_matrix : Tensor, label_vector : Tensor):
      # data must be of shape (n, m), a matrix
      # label vector must be of shape (n), a vector
      # data and labels must be in order
      # test will return a metric and a loss.
      ##### tqdm
      
    def predict(self, batch_size, data_matrix : Tensor):
      # data must be of shape (n, m), a matrix
      # pred will generate a label_vector shaped (n), and that will be the output
      ###### tqdm
    
    def save(self, file_name):
      # file_name must be a txt file in the same directory, lemons will siply write the network weight matrix.
      with open(f"{file_name}.txt", "w") as f:
        f.write(f"{self.network}")
      
      
      
      
      
      
      
      
      

# substract optimizer from weight (each cost func is with respect to one weight, so that will be the weight to be changed)
