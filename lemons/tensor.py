
class tensor:
  def __init__(self, form=(0, 1), shape=(2), data=[1, 1], flatten=False, **kwargs):
    self.form = form
    self.shape = shape
    self.data = data
    self.variables = []
    for var in kwargs:
      self.variables.append(var)
    if flatten == True:
      
      
    
  @property 
  def form(self):
    return self.form
  
  @property
  def shape(self):
    return self.shape
  
  @property
  def data(self):
    return self.data
  
  @staticmethod
  def _shape(data):
    
    
  def dot(self, t):
    #tensor dot
    pass
  
  @staticmethod
  def build(form=(0, 1), shape=(2), data=[1, 1]):
    # take flattened and build tensor
    pass
  
  @classmethod
  def flatten(cls, **kwargs):
    flattened = []
    ##create flattened data
    t = tensor(form=(0, 1), shape=(len(flattened)), data=flattened, flatten=False, **kwargs)
    return t
  
  def __str__(self):
    return 

