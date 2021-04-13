class notshape(Exception):
  """
    Raised when the shape passed into tensor does not match with the data given
  """
  pass

class numnortensor(Exception):
  """
    Raised when the input is neither a num nor a tensor
  """
  pass

class shapeform(Exception):
  """
    Raised when the shape or form are not matching with that of another tensor
  """
  pass
