import math
import os
import random
from lemons.layer import Layer 
from lemons.loss import Loss
from lemons.optimizer import Optimizer
from lemons.metric import Metric
from lemons.activation import Activation
from lemons.tensor import Tensor
from random import random 
"""
NN ->
  FNN ->
    view 
    back
    foward
    train
    test
    predict
    save
    open
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
          ll = self.layer_list[i-1].size
        l = self.layer_list[i+1].layer_weight_tensor(ll)
        self.weight_tensor.append(l)
      # input length
      self.input_length = input_length
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
        ll = self.layer_list[i].size
        lll = self.layer_list[i+1].size
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
        for nindx, neuron in enumerate(self.layer_results[lindx]):
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
      # stuff for next backprop
      self.layer_results = []
      self.layer_results_after_activation = []
      length = len(self.layer_list)
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
    
    def foward(self, data_vector, store=True):
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
          if store:
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

    def train(self, batch_size, epochs, data_tensor : Tensor, label_tensor : Tensor, epoch_show=True, batch_show=True, sample_show=False):
      # data must be a matrix with each row vector being 1 input
      # label must be a matrix with each row vector being one output
      # show will display:
      # epoch loss, metric, progress
      # train will print a final loss and metric
      # loss history will be stored on a list on as an object of the network "self.history"
      old_train_data = data_tensor.data
      old_train_labels = label_tensor.data
      lll = len(old_train_data)
      train_data = []
      train_labels = []
      do = True
      while do:
        if len(old_train_data) >= batch_size:
          x = old_train_data[0:batch_size]
          y = old_train_labels[0:batch_size]
          for p in range(batch_size):
            old_train_data.pop(0)
            old_train_labels.pop(0)
        else:
          do = False
      print(f"given data samples: {lll}, trainable data samples: {lll - len(old_train_data)}")
      # epoch progress
      epoch_loss_history = []
      epoch_metric_history = []
      for epoch in range(epochs):
        # batch progress
        batch_loss_history = []
        batch_metric_history = []
        for bindx, data_batch in enumerate(train_data):
          # sample progress
          sample_loss_history = []
          sample_metric_history = []
          label_batch = train_labels[bindx]
          for sindx, sample in data_batch:
            # comp stuff
            label = label_batch[sindx]
            predicted_label = self.foward(sample)
            loss = self.loss.comp(label, predicted_label)
            metric = self.metric.comp(label, predicted_label)
            # individual progress
            sample_loss_history.append(loss)
            sample_metric_history.append(metric)
            if sample_show:
              print(f"--- sample --- loss: {loss} metric: {metric} progress: {sindx/len(data_batch)}%")
            # perform backprop
            self.back()
          # display progress
          if batch_show:
              print(f"--- batch --- loss: {sum(sample_loss_history)/len(sample_loss_history)} metric: {sum(sample_metric_history)/len(sample_metric_history)} progress: {bindx/len(train_data)}%")
          batch_loss_history.append(sum(sample_loss_history)/len(sample_loss_history))
          batch_metric_history.append(sum(sample_metric_history)/len(sample_metric_history))
        # display progress
        if epoch_show:
            print(f"--- epoch --- loss: {sum(batch_loss_history)/len(batch_loss_history)} metric: {sum(batch_metric_history)/len(batch_metric_history)} progress: {epoch/epochs}%")
        epoch_loss_history.append(sum(batch_loss_history)/len(batch_loss_history))
        epoch_metric_history.append(sum(batch_metric_history)/len(batch_metric_history))
      # end
      print(f"final loss: {epoch_loss_history[-1]}, final metric: {epoch_metric_history[-1]}")
      # retuns final loss and final metric
      return epoch_loss_history[-1], epoch_metric_history[-1]

    def test(self, data_tensor : Tensor, label_tensor : Tensor, show=True):
      # data
      data = data_tensor.data
      labels = label_tensor.data
      loss_history, metric_history = [], []
      for indx, sample in enumerate(data):
        predicted = self.foward(sample)
        right = labels[indx]
        loss = self.loss.comp(right, predicted)
        metric = self.metric.comp(right, predicted)
        loss_history.append(loss)
        metric_history.append(metric)
        if show:
          print(f"predicted: {predicted}, actual: {right}")
          print(f"loss: {loss} metric: {metric}")
          print("-")
      return loss_history, metric_history
      
      
    def predict(self, input_vector):
      return self.foward(input_vector)
    
    def save(self, file_name):
      # file_name must be a txt file in the same directory, lemons will write as follows
      #bias tensor 
      #weight tensor
      f = open(f"{file_name}.txt", "w")
      f.write(f"{self.bias_tensor}")
      f.write(f"{self.weight_tensor}")

    def open(self, file_name):
      with open(f"{file_name}.txt") as file_in:
        lines = []
        for line in file_in:
          lines.append(line)
        self.bias_tensor = eval(lines[0])
        self.weight_tensor = eval(lines[1])
      
      
      
      
      
      
      
      

# substract optimizer from weight (each cost func is with respect to one weight, so that will be the weight to be changed)
