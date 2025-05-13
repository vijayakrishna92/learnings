# forward pass

import torch
import torch.nn as nn
import torch.optim as optim

class SimpleNN(nn.Module):
    def __init__(self):
        super().__init__() 
        self.conv = nn.Conv2d(1, 16, kernel_size=3, padding=1) 
        self.relu = nn.ReLU()  
        self.flatten = nn.Flatten()
        self.fc = nn.Linear(16 * 32 * 32, 2)  

    def forward(self, x): # forward pass
        # forward pass is where the model makes predictions
        # when instance of the model is created, the forward method is called which is this function
        # x is the input tensor
        x = self.conv(x)       
        x = self.relu(x)       
        x = self.flatten(x)    
        x = self.fc(x)         
        return x

model = SimpleNN()
output = model(torch.randn(4, 1, 32, 32)) # forward pass is where the model makes predictions