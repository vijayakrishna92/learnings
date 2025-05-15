import torch
import torch.nn as nn

# Simple model and input
model = nn.Linear(2, 1)  # A simple linear layer
inputs = torch.tensor([[1.0, 2.0]], requires_grad=True)  # Input with gradients enabled
target = torch.tensor([[1.0]])  # Target output

# Forward pass
output = model(inputs)
loss = nn.MSELoss()(output, target)

# Backward pass
#It computes the gradients of the loss with respect to all the learnable parameters in your model using backpropagation. For every nn.Parameter in your model, it computes the gradient of the loss with respect to that parameter and stores it in param.grad.
loss.backward()  # <<< This is the key line

# Inspect gradients
print("Gradients for model weights:")
print(model.weight.grad)
print("Gradients for input:")
print(inputs.grad)