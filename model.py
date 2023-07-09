import torch
import torch.nn as nn

class NeuralNet(nn.Module):
    def __init__(self,input_size,hidden_size,num_classes):
        super(NeuralNet, self).__init__()
        self.a1 = nn.Linear(input_size,hidden_size)
        self.a2 = nn.Linear(hidden_size, hidden_size)
        self.a3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()

    def forward(self,x):
        out = self.a1(x)
        out = self.relu(out)
        out = self.a2(out)
        out = self.relu(out)
        out = self.a3(out)
        return out