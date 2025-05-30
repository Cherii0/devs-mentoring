
# class based decorator
class Logged:

   def __init__(self, func):
      self.func = func

   def __call__(self, *args):
      result = self.func(*args) # executed return 3 + len(args) = 6
      print(f"you called {self.func.__name__}{args} it returned {result}")

# function based decorator
def logged(func):
   def inner_func(*args):
      result = func(*args)
      print(f"you called {func.__name__}{args} it returned {result}")
   return inner_func


@Logged
def function(*args):
   return 3 + len(args) 


function(4, 4, 4)
function(4, 4, 2)
function(4, 1, 1,  1)
