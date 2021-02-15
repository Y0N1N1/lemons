<p align="center">
  <img src="https://github.com/Y0N1N1/lemons/blob/main/docs/assets/images/lemonslogo.png?raw=true" height="200" />
</p>

--------------------------------------------------------------------

# lemons

Lemons is a python library for the non-normies of the dl community. It is dependencies free and only uses python built-in libraries. You can help and use the code at any time under the mit license, all helps apreciated! 

### lemons is dependencies free!

no more 
```bash
pip install -r requirements.txt
```

### Use
for package installs you use:
```bash
pip3 install https://github.com/Y0N1N1/lemons.git --upgrade
```
### Motivation
The main frameworks for building neural nets that give a great level of freedom are obviously Tensorflow, Keras, PyTorch and others, yet these offer solutions in a very standardized way where the users can only choose from the options offered. Lemons aims to offer a less professional approach, where anyone in the community can write other optimizers, loss functions, activation functions, neural networks, and lemons will simply be a library with the purpose to have any models for anyone. Implementations of all kinds of models will be accepted. A future plan would be to have a machine learning marketplace where anyone can post models for free.

### Example
Here is a simple NN example
```python
import lemons as lm
from lemons.loss import Loss
from lemons.optimizer import Optimizer
from lemons.metric import Metric
from lemons.layer import Layer
from lemons.nn import NN
from lemons.tensor import Tensor

cross_entropy = Loss.cross_entropy(2) # 2 because there are 2 classes
adam = Optimizer.adam(0.001, 0.001, 0.9, 0.99) # learning_rate, fudge_factor,decay_rate_one, decay_rate_two 
acc = Metric.acc

activation = Activation.sigmoid
l1 = Layer.dense(10000, activation)
l2 = Layer.dense(7000, activation)
l3 = Layer.dense(300, activation)
l4 = Layer.dense(2, activation)

# build net
network = NN.FNN(cross_entropy, adam, acc, [l1, l2, l3, l4])

# train
data_matrix, label_vector = Tensor([--]), Tensor([--]) # plug data here

batch, epoch = 10, 30000
network.train(batch, epoch, data_matrix, label_vector)
# prints current loss, epoch, acc

# save
network.save('model.txt')
# model.txt must already be a file
# will save the weight matrix 
```
Or if you prefer
```python
import lemons as lm
from lemons.loss import Loss
from lemons.optimizer import Optimizer
from lemons.metric import Metric
from lemons.layer import Layer
from lemons.nn import NN
From lemons.tensor import Tensor

data_matrix, label_vector = Tensor([--]), Tensor([--]) # plug data here

class net:
  def __init__(self):
    self.cross_entropy = Loss.cross_entropy(2) # 2 because there are 2 classes
    self.adam = Optimizer.adam(0.001, 0.001, 0.9, 0.99) # learning_rate, fudge_factor,decay_rate_one, decay_rate_two 
    self.acc = Metric.acc
    activation = Activation.sigmoid
    l1 = Layer.dense(10000, activation) 
    l2 = Layer.dense(7000, activation)
    l3 = Layer.dense(300, activation)
    l4 = Layer.dense(2, activation)
    self.network = [l1, l2, l3, l4]
  
  def build(self):
    # build net
    self.network = NN.FNN(self.cross_entropy, self.adam, self.acc, self.network)
  
  def train(self, data_matrix, label_vector):
    # train
    batch, epoch = 10, 30000
    self.network.train(batch, epoch, data_matrix, label_vector)
  
  def save(self, txt_name):
    self.network.save(f'{txt_name}')
  
first = net()
first.train(data_matrix, label_vector)
# prints current loss, epoch, acc
first.save('model.txt')
```
## Help
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
## License
[MIT](https://choosealicense.com/licenses/mit/)
Please respect the license.
## Architecture
Lemons's architecture is pretty basic, it works with Tensor objects for data, where the data is a data_matrix of shape (n, m), and labels are a vector label_vector of shape (n). A further diagram on the training process is as follows:
----- to do -----
Lemons's network architecture is a matrix containing each layer and it's respective weights, stored in the commonly used .h5 file type.

## save
lemons likes to keep it simple and save the network as a weight matrix on some txt file, they are easy to operate in and don't require any modules, example:
```python
# save
...
network.save('model.txt')
# model.txt must already be a file
# will save the weight matrix 
```

## To Do

- make loss.grad_comp
- make actvation.grad_comp
- make layer.grad_comp
- make layer.bias_grad_comp
- make layer_results and layer_results_after_activation with foward, foward
- make train, test, pred
- check activation
- make layer with res and res_actv for all layer and check layers
- check loss
- check metric
- improve metric
- check optimizer
- check tensor
- check utils
- make first launch
