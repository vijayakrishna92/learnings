# defining model using torch.nn
import torch
import torch.nn as nn # neural network module

class SimpleModel(nn.Module): # defining a class for the model, inheriting from nn.Module
    # constructor method
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(10, 5) # defining a linear layer with 10 input features and 5 output features
    
    def forward(self, x): # defining the forward pass
        x = self.linear(x)
        return x

model = SimpleModel() # creating an instance of the model
print(model) # printing the model architecture
# The model consists of a single linear layer that takes 10 input features and outputs 5 features.
# The forward method defines how the input data flows through the model.
input_data = torch.randn(1, 10) # creating a random input tensor with shape (1, 10)
output_data = model(input_data) # passing the input data through the model
print(output_data.shape) # printing the output data shape
# The output data is a tensor with shape (1, 5), which is the result of applying the linear layer to the input data.
# The model can be trained using a loss function and an optimizer, which are not included in this example.