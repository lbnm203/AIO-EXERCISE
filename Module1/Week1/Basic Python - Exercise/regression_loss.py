import random
import math

def regression_loss_func():
     num_samples = input('num_samples: ')
     
     if not num_samples.isnumeric():
          print('number of samples must be an integer number')
          return
     
     loss_name = input('loss name: ')    
     num_samples = int(num_samples)

     valid_loss = ['MAE','MSE','RMSE']
     if loss_name not in valid_loss:
          print(f'{loss_name} is not support')

     target = [random.uniform(0, 10) for _ in range(num_samples)]
     pred = [random.uniform(0, 10) for _ in range(num_samples)]

     if loss_name == 'MAE':
          loss_sample = [abs(target[i] - pred[i]) for i in range(num_samples)]
          overall_loss = sum(loss_sample) / num_samples
     elif loss_name == 'MSE':
          loss_sample = [(target[i] - pred[i])**2 for i in range(num_samples)]
          overall_loss = sum(loss_sample) / num_samples
     elif loss_name == 'RMSE':
          loss_sample = [(target[i] - pred[i])**2 for i in range(num_samples)]
          overall_loss = math.sqrt(sum(loss_sample) / num_samples)       
          
     for i in range(num_samples):
          print(f'loss_name: {loss_name}, sample: {i}, pred: {pred[i]}, target: {target[i]}, loss: {loss_sample[i]}')
     
     print(f'Final RMSE: {overall_loss}')

regression_loss_func()
