import math

def is_number(n) :
     try :
          float(n)  # Type - casting the string to ‘float ‘.
                    # If string is not a valid ‘float ‘ ,
                    # it ’ll raise ‘ValueError ‘ exception
     except ValueError:
          return False
     return True


def activation_func(x, activation_function):   
     x = float(x)
     if activation_function == 'sigmoid':
          sigmoid = 1 / (1 + math.exp(-x))
          print(f'{activation_function}: f({x}) = {sigmoid}')
     elif activation_function == 'relu':
          if x <= 0:
               result = 0
               print(f'{activation_function}: f({x}) = {result}')
          else:
               print(f'{activation_function}: f({x}) = {x}')             
     elif activation_function == 'elu':
          if x <= 0:
               alpha = 0.01
               result = alpha * (math.exp(x) - 1)
               print(f'{activation_function}: f({x}) = {result}')
          else:
               print(f'{activation_function}: f({x}) = {x}')
     else:
          print(f'{activation_function} is not supported')


x = input('x = ')

if not is_number(x):
     print('x must be a number')
else:
     activation_function = input('activation_function (sigmoid | relu | elu) = ')
     activation_func(x, activation_function)
          