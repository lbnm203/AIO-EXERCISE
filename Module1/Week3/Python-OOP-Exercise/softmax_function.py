import torch
import torch.nn as nn


class softmax_func(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, data):
        xi = torch.exp(data)
        sum_exp_xi = torch.sum(xi)
        return xi / sum_exp_xi


class softmax_stable_func(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, data):
        xi = torch.exp(data - max(data))
        sum_exp_xi = torch.sum(xi)
        return xi / sum_exp_xi


data = torch.Tensor([1, 2, 3])
softmax = softmax_func()
output = softmax(data)
print(output)

softmax_stable = softmax_stable_func()
output1 = softmax_stable(data)
print(output1)
