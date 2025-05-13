import torch
import torch.nn as nn
import torch.optim as optim
import random
import numpy as np

# 1. Set seed for reproducibility
def set_seed(seed=42):
    torch.manual_seed(seed)
    random.seed(seed)
    np.random.seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

set_seed(42)

# 2. Define the model
class SimpleNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(1, 16, kernel_size=3, padding=1)
        self.relu = nn.ReLU()
        self.flatten = nn.Flatten()
        self.fc = nn.Linear(16 * 32 * 32, 2)  # 2 output classes

    def forward(self, x):
        x = self.conv(x)
        x = self.relu(x)
        x = self.flatten(x)
        x = self.fc(x)
        return x

# 3. Device setup
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 4. Create synthetic data
inputs = torch.randn(4, 1, 32, 32).to(device)        # 4 images, 1 channel, 32x32
labels = torch.tensor([0, 1, 1, 0]).to(device)       # 4 labels for 2-class task

# 5. Initialize model, loss, optimizer
model = SimpleNN().to(device)
loss_fn = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 6. Training loop (2 epochs)
for epoch in range(2):
    model.train()

    # Forward pass
    outputs = model(inputs)
    loss = loss_fn(outputs, labels)

    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")