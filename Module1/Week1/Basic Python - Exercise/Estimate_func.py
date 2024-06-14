import math

def factorial(number):
     if number == 0 or number == 1:
          return 1
     result = 1
     for i in range(2, number+1):
          result *= i
     return result

def estimate_sin(x, n):
     result = 0
     for i in range(n):
          values = (pow((-1),i) * pow(x, (2*i + 1))) / factorial(2*i + 1)
          result += values
     return result

def estimate_cos(x, n):
     result = 0
     for i in range(n):
          values = (pow((-1),i) * pow(x, (2*i))) / factorial(2*i)
          result += values
     return result

def estimate_sinh(x, n):
     result = 0
     for i in range(n):
          values = pow(x, (2*i + 1)) / factorial(2*i + 1)
          result += values
     return result

def estimate_cosh(x, n):
     result = 0
     for i in range(n):
          values = pow(x, (2*i)) / factorial(2*i)
          result += values
     return result

x = float(input('x= '))
n = int(input('n= '))

print(estimate_sin(x, n))
print(estimate_cos(x, n))
print(estimate_sinh(x, n))
print(estimate_cosh(x, n))