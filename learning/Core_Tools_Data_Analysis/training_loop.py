import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

# 1. Define your model
class SimpleNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(1, 16, 3, padding=1)
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

# 2. Loss function and optimizer
loss_fn = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 3. Create dummy dataset and dataloader
images = torch.randn(100, 1, 32, 32)     # 100 grayscale images
labels = torch.randint(0, 2, (100,))     # Binary class labels: 0 or 1
dataset = TensorDataset(images, labels)
dataloader = DataLoader(dataset, batch_size=4, shuffle=True)

# 4. Training loop
epochs = 5
for epoch in range(epochs):
    model.train()
    for batch in dataloader:
        inputs, labels = batch

        optimizer.zero_grad()           # Clear gradients
        outputs = model(inputs)         # Forward pass
        loss = loss_fn(outputs, labels) # Compute loss
        loss.backward()                 # Backward pass
        optimizer.step()                # Update weights

    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")