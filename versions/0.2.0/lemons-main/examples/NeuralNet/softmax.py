import lemons as lm
from lemons import tensor
def softmax(vec : tensor):
  vec = vec.data
  new = []
  under = 0
  for element in vec:
    under += lm.exp(element)
  for element in vec:
    new.append(lm.exp(element)/under)
  return tensor(data=new)
