<img src="https://github.com/Y0N1N1/lemons/blob/main/docs/assets/images/lemonslogo.png?raw=true" height="200" />

# lemons
### lemons is dependencies free!

Lemons is a python library for the non-normies of the dl community. It is dependencies free and only uses python built-in libraries. You can help and use the code at any time under the mit license, all helps apreciated! 

### Use
for package installs you use:
```
pip3 install git+https://github.com/Y0N1N1/lemons.git --upgrade
```
### Motivation
The main frameworks for building neural nets that give a great level of freedom are obviously Tensorflow, Keras, PyTorch and others, yet these offer solutions in a very standardized way where the users can only choose from the options offered. Lemons aims to offer a less professional approach, where anyone in the community can write other optimizers, loss functions, activation functions, neural networks, and lemons will simply be a library with the purpose to have any models for anyone. Implementations of all kinds of models will be accepted. A future plan would be to have a machine learning marketplace where anyone can post models for free.

### Example
Here is a simple NN example
```python
import lemons as lm 
# still to do 
```
## Help
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
## License
[MIT](https://choosealicense.com/licenses/mit/)
Please respect the license.
## Architecture
Lemons's architecture is pretty basic, it works with Tensor objects for data, where the data is a data_matrix of shape (n, m), and features are a vector feature_vector of shape (n). A further diagram on the training process is as follows:
----- to do -----
Lemons's network architecture is a matrix containing each layer and it's respective weights, stored in the commonly used .h5 file type.
## To Do

- make loss.grad_comp
- make actvation.grad_comp
- make layer.grad_comp
- make layer.bias_grad_comp
- make layer_results and layer_results_after_activation with foward, foward
- make train, test, predict
