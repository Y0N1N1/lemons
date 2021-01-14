"""
Error ->
  custom
  try_except_else
  raise_error
Error list ->
  AssertionError			#Raised when assert statement fails.
  AttributeError			#Raised when attribute assignment or reference fails.
  EOFError				#Raised when the input() functions hits end-of-file condition.
  FloatingPointError		#Raised when a floating point operation fails.
  GeneratorExit			#Raise when a generator's close() method is called.
  ImportError				#Raised when the imported module is not found.
  IndexError				#Raised when index of a sequence is out of range.
  KeyError				#Raised when a key is not found in a dictionary.
  KeyboardInterrupt		#Raised when the user hits interrupt key (Ctrl+c or delete).
  MemoryError				#Raised when an operation runs out of memory.
  NameError				#Raised when a variable is not found in local or global scope.
  NotImplementedError		#Raised by abstract methods.
  OSError					#Raised when system operation causes system related error.
  OverflowError			#Raised when result of an arithmetic operation is too large to be represented.
  ReferenceError			#Raised when a weak reference proxy is used to access a garbage collected referent.
  RuntimeError			#Raised when an error does not fall under any other category.
  StopIteration			#Raised by next() function to indicate that there is no further item to be returned by iterator.
  SyntaxError				#Raised by parser when syntax error is encountered.
  IndentationError		#Raised when there is incorrect indentation.
  TabError				#Raised when indentation consists of inconsistent tabs and spaces.
  SystemError				#Raised when interpreter detects internal error.
  SystemExit				#Raised by sys.exit() function.
  TypeError				#Raised when a function or operation is applied to an object of incorrect type.
  UnboundLocalError		#Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.
  UnicodeError			#Raised when a Unicode-related encoding or decoding error occurs.
  UnicodeEncodeError		#Raised when a Unicode-related error occurs during encoding.
  UnicodeDecodeError		#Raised when a Unicode-related error occurs during decoding.
  UnicodeTranslateError	#Raised when a Unicode-related error occurs during translating.
  ValueError				#Raised when a function gets argument of correct type but improper value.
  ZeroDivisionError		#Raised when second operand of division or modulo operation is zero.
"""

class Error:
  def __init__(self, custom_message):
    self.custom_message = custom_message

  def custom(self):
    raise Exception(str(self.custom_message))
    
  def try_except_else(self, try_message, except_list, except_answer_list, else_message):
    for i in except_list:
      try:
        exec(str(try_message))
      except i:
        print(except_answer_list[i])
      else:
        print(else_message)
  
  def raise_error(self, error_type):
    exec(f"raise {error_type}({self.custom_message})")
  
      
      
  
