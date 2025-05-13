# optimizers
# optimizers are algorithms or methods used to change the attributes of the neural network such as weights and learning rate in order to reduce the losses.
# They are used in training the model. The goal of an optimizer is to minimize the loss function by adjusting the weights of the model.
# 1. SGD (Stochastic Gradient Descent) optimizer = optim.Adam(model.parameters(), lr=0.001)
# 2. Adam (Adaptive Moment Estimation) optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
# 3. RMSprop (Root Mean Square Propagation) optimizer = optim.RMSprop(model.parameters(), lr=0.01, alpha=0.99)
# 4. Adagrad (Adaptive Gradient Algorithm) optimizer = optim.Adagrad(model.parameters(), lr=0.01)
# 5. AdamW (Adam with Weight Decay) optimizer = optim.AdamW(model.parameters(), lr=0.001, weight_decay=0.01)
# 6. Adadelta (Adaptive Delta) optimizer = optim.Adadelta(model.parameters(), lr=0.01, rho=0.9)
# 7. FTRL (Follow The Regularized Leader) optimizer = optim.FTRL(model.parameters(), lr=0.01, l1=0.01, l2=0.01)

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

    def forward(self, x):
        x = self.conv(x)       
        x = self.relu(x)       
        x = self.flatten(x)    
        x = self.fc(x)         
        return x

model = SimpleNN()
output = model(torch.randn(4, 1, 32, 32)) 
loss = nn.CrossEntropyLoss()

optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

# Example usage
targets = torch.tensor([1, 0, 1, 0])  # Example target labels
loss_value = loss(output, targets)
print("Loss:", loss_value.item())
optimizer.zero_grad()  # Zero the gradients
loss_value.backward()  # Backpropagation
optimizer.step()  # Update the weights

'''
Scenario	Optimizer
Small dataset, tabular data	Adam
CNN on images (vision)	SGD with momentum, Adam
NLP with Transformers	AdamW
Sparse data or embeddings	Adagrad, FTRL
RNNs, LSTMs	RMSprop, Adam
Fine-tuning pretrained model	SGD, AdamW
'''